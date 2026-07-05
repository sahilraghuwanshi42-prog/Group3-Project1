from rest_framework import serializers
from .models import Document, ExtractedClause, RiskFlag

class UploadDocuemntSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 255)
    pdf_file = serializers.FileField()

    
class ExtractedClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedClause
        fields = "__all__"


class RiskFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFlag
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    clauses = ExtractedClauseSerializer(
        source="extractedclause_set",
        many=True,
        read_only=True
    )

    risk_flags = RiskFlagSerializer(
        source="riskflag_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "pdf_file",
            "uploaded_at",
            "clauses",
            "risk_flags",
        ]