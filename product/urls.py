from . import views
from django.urls import path


urlpatterns = [
    # URL to display the prospect detail
    path(
        '',
        views.product_index,
        name='product_index'
    ),
]
