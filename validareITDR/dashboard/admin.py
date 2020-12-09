from django.contrib import admin
from .models import Store, GroupStore, Product, Campaign

admin.site.register(Store)
admin.site.register(GroupStore)
admin.site.register(Product)
admin.site.register(Campaign)