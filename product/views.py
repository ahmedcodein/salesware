from .models import Product
from django.views import generic
from django.shortcuts import render, get_object_or_404

# Create your views here.


class ProductList(generic.ListView):
    """
    The view handles the presentations of all the products
    in the database
    """
    queryset = Product.objects.all().order_by('name')
    template_name = "product/product_list.html"


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    # Collect the product id and save it
    # to be accessed later by other views
    request.session['product_id'] = id

    return render(
        request,
        "product/product_detail.html",
        {"product": product}
    )
