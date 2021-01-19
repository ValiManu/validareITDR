from django.contrib import admin
from .models import Shop, Network, Product, PromotionalCampaign, Address, Prize

admin.site.register(Shop)
admin.site.register(Network)
admin.site.register(Address)


@admin.register(Product)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'promotional_campaign', 'url_img', 'active_product')


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'promotional_campaign', 'url_img', 'id', 'shop', 'active_product', 'quantity', 'min', 'max')


@admin.register(PromotionalCampaign)
class PromotionalCampaign(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'selected_campaign')
