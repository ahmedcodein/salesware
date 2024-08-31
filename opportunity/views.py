from django.views import generic
from .models import Opportunity

# Create your views here.


class OpportunityList(generic.ListView):
    """
    The view handles the presentations of all the opportunities
    in the database
    """
    queryset = Opportunity.objects.all().order_by('name')
    template_name = "opportunity/opportunity_list.html"
    paginate_by = 15
