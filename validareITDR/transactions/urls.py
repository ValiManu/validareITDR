from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('ticket-validation', views.is_ticket_in_use, name='ticket_validation'),
    path('product-validation', views.is_product_in_use, name='product_validation'),
    path('save-data', views.save_data, name='save_data')
]
