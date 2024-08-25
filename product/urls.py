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
]
