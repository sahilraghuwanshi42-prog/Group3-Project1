from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    extract_text = models.TextField(blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ExtractedClause(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='clauses'
    )
    clause_text = models.TextField()
    clause_type = models.CharField(max_length=100)

    def __str__(self):
        return self.clause_type


class RiskFlag(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='risk_flags'
    )
    risk_text = models.TextField()
    risk_level = models.CharField(max_length=50)

    def __str__(self):
        return self.risk_level