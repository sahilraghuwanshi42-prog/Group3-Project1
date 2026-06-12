from django.contrib import admin
from .models import Document, ExtractedClause, RiskFlag

admin.site.register(Document)
admin.site.register(ExtractedClause)
admin.site.register(RiskFlag)