from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('ajax_response', views.ajax_response, name='ajax')
]
