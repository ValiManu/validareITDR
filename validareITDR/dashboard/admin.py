from django.contrib import admin
from .models import Shop, Network, Product, PromotionalCampaign, Address, Prize

admin.site.register(Shop)
admin.site.register(Network)
admin.site.register(PromotionalCampaign)
admin.site.register(Address)
admin.site.register(Prize)


@admin.register(Product)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_img', 'active_product', 'promotional_campaign')
