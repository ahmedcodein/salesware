from django.shortcuts import render
from django.views import generic
from .models import Account


# Create your views here.
class AccountList(generic.ListView):
    queryset = Account.objects.all().order_by('company')
    template_name = "sales_databases/accounts.html"
