from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Document

class UploadDocumentView(APIView):
    def post(self, request):
        title = request.data.get("title")
        pdf_file = request.FILES.get("pdf_file")

        document = Document.objects.create(
            title=title,
            pdf_file=pdf_file
        )

        return Response({
            "id": document.id,
            "title": document.title,
            "pdf_file": document.pdf_file.url
        }, status=status.HTTP_201_CREATED)