from django.contrib import admin
from .models import Prospect
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Prospect)
class ProspectAdmin(SummernoteModelAdmin):
    list_display = (
        'company',
        'first_name',
        'last_name',
        'email',
        'title',
        'industry',
        'country',
        'owner',
        'created_on'
    )
    search_fields = ['company']
    list_filter = ('company',)
