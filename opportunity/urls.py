from . import views
from django.urls import path


urlpatterns = [
    # URL to display the opportunity detail
    path(
        '',
        views.OpportunityList.as_view(),
        name='opportunity_list'
    ),
    # URL to display the opportunity detail
    path(
        'opportunity_detail/<int:id>/',
        views.opportunity_detail,
        name='opportunity_detail'
    ),
    path(
        'opportunity_create/',
        views.opportunity_create,
        name='opportunity_create'
    ),
    path(
        'opportunity_edit/',
        views.opportunity_edit,
        name='opportunity_edit'
    ),
]
