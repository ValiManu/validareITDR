from django.contrib import admin
from .models import Sales, ProductsSold


# admin.site.register(Sales)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket_no', 'ticket_date', 'shop', 'prize')


@admin.register(ProductsSold)
class ProductsSoldAdmin(admin.ModelAdmin):
    list_display = ('sale_id', 'product', 'quantity')

