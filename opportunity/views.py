from django.views import generic
from django.shortcuts import render
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


def opportunity_create(request):
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
