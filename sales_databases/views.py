from .models import Prospect
from django.views import generic
from django.shortcuts import render, get_object_or_404


# Create your views here.
class ProspectIndex(generic.ListView):
    queryset = Prospect.objects.all().order_by('company')
    template_name = "sales_databases/prospects_index.html"


def prospect_detail(request, id):
    prospect = get_object_or_404(Prospect, pk=id)

    return render(
        request,
        "sales_databases/prospect_detail.html",
        {"prospect": prospect}
    )
