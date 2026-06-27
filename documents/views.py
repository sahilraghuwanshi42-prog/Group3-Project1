from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Document, ExtractedClause
from .pdf_utils import extract_text_from_pdf, extract_clauses


class UploadDocumentView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        title = request.data.get("title")
        pdf_file = request.FILES.get("pdf_file")

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
            

        return Response({
            "id": document.id,
            "title": document.title,
            "pdf_file": document.pdf_file.url,
            "text_preview": document.extract_text[:1000]
        }, status=status.HTTP_201_CREATED)