from .models import Product
from .forms import ProductForm
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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


def product_create(request):
    """
    This view handles two requests: Get and Post
    If Post, it handles the creation of new
    product and save it to the database
    """
    if request.method == 'POST':
        new_product = ProductForm(request.POST)
        if new_product.is_valid():
            product = new_product.save(commit=False)
            product.owner = request.user
            product.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new product is successfully saved!'
                }
            )
        else:
            for field, errors in new_product.errors.as_data().items():
                for error in errors:
                    print(error.code)
                    if error.code == 'required':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Product {field.capitalize()}
                                field is required!
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
                                This Product {field.capitalize()}
                                already exists!
                                """
                            }
                        )
                    elif error.code == 'invalid':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Product {field.capitalize()}
                                must be a number!
                                """

                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The Product {field.capitalize()}
                                has the following error: {error}!
                                """
                            }
                        )

    else:
        new_product = ProductForm()
        return render(
            request,
            'product/product_create.html',
            {
                'new_product': new_product
            }
        )
