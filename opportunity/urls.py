from . import views
from django.urls import path


urlpatterns = [
    # URL to display the opportunity detail
    path(
        '',
        views.OpportunityList.as_view(),
        name='opportunity_list'
    ),
    path(
        'opportunity_create/',
        views.opportunity_create,
        name='opportunity_create'
    ),
]
