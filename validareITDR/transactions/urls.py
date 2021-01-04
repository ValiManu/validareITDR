from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('ticket-validation', views.ticket_validation, name='ticket_validation'),
    path('product-validation', views.product_validation, name='product_validation'),
    path('save-data', views.save_data, name='save_data')
]
