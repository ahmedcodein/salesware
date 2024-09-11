from django.urls import path
from . import views


urlpatterns = [
    # URL to display the home page
    path(
        '',
        views.home,
        name='home'
    ),
    # URL to display the contact page
    path(
        'contact/',
        views.contact,
        name='contact'
    ),
]
