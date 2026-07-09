# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Document, ExtractedClause, RiskFlag
from .pdf_utils import extract_text_from_pdf, extract_clauses

from .pdf_utils import detect_risk

from .serializers import DocumentSerializer,UploadDocuemntSerializer

class UploadDocumentView(GenericAPIView):
    serializer_class = UploadDocuemntSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        title = request.data.get("title")
        pdf_file = request.FILES.get("pdf_file")

        # Validation
        if not title:
            return Response(
                {"error": "Title is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not pdf_file:
            return Response(
                {"error": "PDF file is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not pdf_file.name.lower().endswith(".pdf"):
            return Response(
                {"error": "Only PDF files are allowed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        document = Document.objects.create(
            title=title,
            pdf_file=pdf_file
        )

        text = extract_text_from_pdf(document.pdf_file.path)

        document.extract_text = text
        document.save()

        clauses = extract_clauses(text)

        for clause in clauses:
            from .pdf_utils import categorize_clause

            ExtractedClause.objects.create(
                document=document,
                clause_text=clause,
                # clause_type="General"
                clause_type=categorize_clause(clause)
            )
            risk = detect_risk(clause)

            if risk != "Low":
                RiskFlag.objects.create(
                    document=document,
                    risk_text=clause,
                    risk_level=risk
                )


        serializer = DocumentSerializer(document)

        return Response(
            serializer.data,
                status=status.HTTP_201_CREATED
        )