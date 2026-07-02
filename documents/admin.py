from django.contrib import admin
from .models import Document, ExtractedClause, RiskFlag


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "uploaded_at")
    search_fields = ("title",)
    ordering = ("-uploaded_at",)


@admin.register(ExtractedClause)
class ExtractedClauseAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "clause_type")
    list_filter = ("clause_type",)
    search_fields = ("clause_text",)


@admin.register(RiskFlag)
class RiskFlagAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "risk_level")
    list_filter = ("risk_level",)
    search_fields = ("risk_text",)