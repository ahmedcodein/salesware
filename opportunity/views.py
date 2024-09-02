from django.views import generic
from django.shortcuts import render
from .models import Opportunity
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
    products = Product.objects.all()
    prospects = Prospect.objects.all()
    return render(
        request,
        'opportunity/opportunity_create.html',
        {'prospects': prospects,
         'products': products,
         }
    )
