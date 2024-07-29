from . import views
from django.urls import path


urlpatterns = [
    path('prospects/', views.ProspectIndex.as_view(), name=('prospects')),
]
