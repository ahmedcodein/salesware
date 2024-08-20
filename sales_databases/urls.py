from . import views
from django.urls import path


urlpatterns = [
    # URL to display the list of all the
    # prospect in the database
    path(
        '',
        views.ProspectIndex.as_view(),
        name='prospects'
    ),
    # URL to display the prospect detail
    path(
        'prospect_detail/<int:id>/',
        views.prospect_detail,
        name='prospect_detail'
    ),
    # URL to display New Prospect Form
    # and to submit the new prospect data
    path(
        'create_new_prospect/',
        views.create_new_prospect,
        name='create_new_prospect'
    )
]
