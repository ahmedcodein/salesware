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
    paginate_by = 15


def product_detail(request, id):
    """
    The view handles the display of a product record
    detail
    """
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
        product_create = ProductForm(request.POST)
        if product_create.is_valid():
            product = product_create.save(commit=False)
            product.owner = request.user
            product.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new product is successfully saved!'
                }
            )
        else:
            for field, errors in product_create.errors.as_data().items():
                for error in errors:
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
        product_create = ProductForm()
        return render(
            request,
            'product/product_create.html',
            {
                'product_create': product_create
            }
        )


def product_edit(request):
    """
    This view handles a Post request for updating
    any of the product fields
    """
    if request.method == 'POST':
        product_id = request.session.get('product_id', 'Default Value')
        product = get_object_or_404(Product, pk=product_id)
        product_edit = ProductForm(request.POST, instance=product)
        f_condition = product_edit.is_valid()
        s_condition = product.owner == request.user
        t_condition = request.user.is_superuser
        if f_condition and (s_condition or t_condition):
            product = product_edit.save(commit=False)
            product.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The product is successfully updated!'
                }
            )
        elif product_edit.is_valid() and product.owner is not request.user:
            return JsonResponse(
                {
                    'success': False,
                    'message': 'Update denied, unauthorized user'
                }
            )
        else:
            for field, errors in product_edit.errors.as_data().items():
                for error in errors:
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


def product_delete(request):
    """
    This view handles the delete request of
    a product
    """
    product_id = request.session.get('product_id', 'Default Value')
    product = get_object_or_404(Product, pk=product_id)

    f_condition = product.owner == request.user
    s_condition = request.user.is_superuser

    if f_condition or s_condition:
        product.delete()
        return JsonResponse(
            {
                'success': True,
                'message': "The Product is successfully deleted!"
            }
        )
    else:
        return JsonResponse(
            {
                'success': False,
                'message': 'Deletion denied, unauthorized user'
            }
        )
