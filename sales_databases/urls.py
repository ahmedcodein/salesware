from . import views
from django.urls import path


urlpatterns = [
    path('accounts/', views.AccountList.as_view(), name=('account')),
]
