from .models import Prospect
from .forms import ProspectForm
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


# Create your views here.
class ProspectIndex(generic.ListView):
    """
    The view handles the presentations of all the prospects
    in the database
    """
    queryset = Prospect.objects.all().order_by('company')
    template_name = "sales_databases/prospects_index.html"


def prospect_detail(request, id):
    prospect = get_object_or_404(Prospect, pk=id)

    return render(
        request,
        "sales_databases/prospect_detail.html",
        {"prospect": prospect}
    )


def create_new_prospect(request):
    """
    This view handles two requests: Get and Post
    If Post, it handles the creation of new
    prospect and save it to the database
    """
    if request.method == 'POST':
        new_prospect = ProspectForm(request.POST)
        if new_prospect.is_valid():
            prospect = new_prospect.save(commit=False)
            prospect.owner = request.user
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new prospect is successfully saved!'
                }
            )
        else:
            return JsonResponse(
                {
                    'success': False,
                    'message': 'The record already exists in the database!'
                }
            )
    else:
        new_prospect = ProspectForm()
        return render(
            request,
            'sales_databases/prospect_create.html',
            {
                'new_prospect': new_prospect
            }
        )
