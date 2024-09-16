from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Opportunity
from .forms import OpportunityForm
from prospect.models import Prospect
from product.models import Product

# Create your views here.


class OpportunityList(generic.ListView):
    """
    The view handles the presentations of all the opportunities
    in the database
    """
    queryset = Opportunity.objects.all().order_by('name')
    template_name = "opportunity/opportunity_list.html"
    paginate_by = 15


def opportunity_detail(request, id):
    """
    The view handles the display of an opportunity record
    detail
    """
    opportunity = get_object_or_404(Opportunity, pk=id)
    prospects = Prospect.objects.all()
    products = Product.objects.all()
    # Collect the Opportunity id and save it
    # to be accessed later by other views
    request.session['opportunity_id'] = id

    return render(
        request,
        "opportunity/opportunity_detail.html",
        {
            "opportunity": opportunity,
            'prospects': prospects,
            'products': products,
        }
    )


def opportunity_create(request):
    """
    The view handles the creation of new opportunity
    record
    """
    if request.method == 'GET':
        products = Product.objects.all()
        prospects = Prospect.objects.all()
        return render(
            request,
            'opportunity/opportunity_create.html',
            {
                'prospects': prospects,
                'products': products,
            }
        )
    elif request.method == 'POST':
        opportunity_create = OpportunityForm(request.POST)
        if opportunity_create.is_valid():
            opportunity = opportunity_create.save(commit=False)
            opportunity.owner = request.user
            opportunity.is_closed = False
            opportunity.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new opportunity is successfully saved!'
                }
            )
        else:
            for field, errors in opportunity_create.errors.as_data().items():
                for error in errors:
                    if error.code == 'required':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""The Opportunity {field.capitalize()} field
                                is required!
                                Please try again!
                                """
                            }
                        )
                    elif error.code == 'invalid_choice':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                field received invalid choice!
                                Please try again!
                                """

                            }
                        )
                    elif error.code == 'unique':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                already exists in the data base
                                """

                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                has the following error: {error}!
                                Please try again!
                                """
                            }
                        )


def opportunity_edit(request):
    """
    This view handles a Post request for updating
    any of the opportunity fields
    """
    if request.method == 'POST':
        opportunity_id = request.session.get(
            'opportunity_id', 'Default Value')
        opportunity = get_object_or_404(Opportunity, pk=opportunity_id)
        opportunity_edit = OpportunityForm(request.POST, instance=opportunity)
        f_condition = opportunity_edit.is_valid()
        s_condition = opportunity.owner == request.user
        t_condition = request.user.is_superuser
        "If the form is valid, only update if the owner or"
        "the admin requests the update"
        if f_condition and (s_condition or t_condition):
            opportunity = opportunity_edit.save(commit=False)
            opportunity.is_closed = False
            opportunity.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new opportunity is successfully updated!'
                }
            )
        elif f_condition and opportunity.owner is not request.user:
            return JsonResponse(
                {
                    'success': False,
                    'message': 'Update denied, unauthorized user'
                }
            )
        else:
            for field, errors in opportunity_edit.errors.as_data().items():
                for error in errors:
                    if error.code == 'required':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""The Opportunity {field.capitalize()} field
                                is required!
                                Please try again!
                                """
                            }
                        )
                    elif error.code == 'invalid_choice':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                field received invalid choice!
                                Please try again!
                                """

                            }
                        )
                    elif error.code == 'unique':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                already exists in the data base
                                """

                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Opportunity {field.capitalize()}
                                has the following error: {error}!
                                Please try again!
                                """
                            }
                        )


def opportunity_delete(request):
    """
    This view handles the delete request of
    an opportunity record
    """
    opportunity_id = request.session.get('opportunity_id', 'Default Value')
    opportunity = get_object_or_404(Opportunity, pk=opportunity_id)

    f_condition = opportunity.owner == request.user
    s_condition = request.user.is_superuser
    "Only delete if the owner or the admin requests the delete"
    if f_condition or s_condition:
        opportunity.delete()
        return JsonResponse(
            {
                'success': True,
                'message': "The Opportunity is successfully deleted!"
            }
        )
    else:
        return JsonResponse(
            {
                'success': False,
                'message': 'Deletion denied, unauthorized user'
            }
        )
