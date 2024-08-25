from .models import Product
from django.views import generic

# Create your views here.


class ProductList(generic.ListView):
    """
    The view handles the presentations of all the products
    in the database
    """
    queryset = Product.objects.all().order_by('name')
    template_name = "product/product_list.html"
