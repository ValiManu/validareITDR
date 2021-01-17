from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('ticket/in-use/', views.is_ticket_in_use, name='ticket_in_use'),
    path('product/in-use/', views.is_product_in_use, name='product_in_use'),
    path('save/transaction', views.save_transaction, name='save_transaction')
]
