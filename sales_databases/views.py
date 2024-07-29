from django.shortcuts import render
from django.views import generic
from .models import Prospect


# Create your views here.
class ProspectIndex(generic.ListView):
    queryset = Prospect.objects.all().order_by('company')
    template_name = "sales_databases/prospects_index.html"
