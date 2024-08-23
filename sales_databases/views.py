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
    # Collect the prospect id and save it
    # to be accessed later by other views
    request.session['prospect_id'] = id

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
            prospect.save()
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


def prospect_edit(request):
    """
    This view handles a Post request for updating
    any of the prospect fields
    """
    if request.method == 'POST':
        prospect_id = request.session.get('prospect_id', 'Default Value')
        prospect = get_object_or_404(Prospect, pk=prospect_id)
        prospect_edit = ProspectForm(request.POST, instance=prospect)
        f_condition = prospect_edit.is_valid()
        s_condition = prospect.owner == request.user
        t_condition = request.user.is_superuser
        if f_condition and (s_condition or t_condition):
            prospect = prospect_edit.save(commit=False)
            prospect.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The prospect is successfully updated!'
                }
            )
        elif prospect_edit.is_valid() and prospect.owner is not request.user:
            return JsonResponse(
                {
                    'success': False,
                    'message': 'Update denied, unauthorized user'
                }
            )
        else:
            return JsonResponse(
                {
                    'success': False,
                    'message': 'The prospect is not updated!'
                }
            )
