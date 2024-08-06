from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProspectIndex.as_view(), name=('prospects')),
    path('<int:id>/', views.prospect_detail, name='prospect_detail'),
]
