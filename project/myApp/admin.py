from django.contrib import admin
from .models import PredResults

class PredResultsAdmin(admin.ModelAdmin):
    list_display = ('cet', 'gpa', 'strand', 'classification')
    list_filter = ('classification',)
    search_fields = ('cet', 'gpa', 'strand', 'classification')

admin.site.register(PredResults, PredResultsAdmin)


# Register your models here.

