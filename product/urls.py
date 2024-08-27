from . import views
from django.urls import path


urlpatterns = [
    # URL to display the product detail
    path(
        '',
        views.ProductList.as_view(),
        name='product_list'
    ),
    # URL to display the product detail
    path(
        'product_detail/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),
    # URL to display New Product Form
    # and to submit the new Product data
    path(
        'product_create/',
        views.product_create,
        name='product_create'
    ),
    path(
        'product_edit/',
        views.product_edit,
        name='product_edit'
    ),
]
