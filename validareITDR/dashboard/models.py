from django.conf import settings
from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=30, verbose_name='Denumire')
    full_name = models.CharField(max_length=30)
    store_address = models.CharField(max_length=40, verbose_name='Adresa')
    store_active = models.BooleanField(verbose_name='Activ', default=True)
    group_store = models.ForeignKey('GroupStore', on_delete=models.SET_NULL, null=True)
    allocate_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['store_name']

    def __str__(self):
        return self.store_name


class GroupStore(models.Model):
    group_store = models.CharField(max_length=20, verbose_name='Grup Magazin')

    def __str__(self):
        return self.group_store


class Product(models.Model):
    product_name = models.CharField(max_length=20, verbose_name='Denumire')
    url_img = models.CharField(max_length=200, verbose_name='URL Img')
    product_active = models.BooleanField(verbose_name='Activ', default=True)
    stock = models.IntegerField(verbose_name="Stoc")
    store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=50, verbose_name='Denumire')
    campaign_start_date = models.DateField(verbose_name='Data Start')
    campaign_end_date = models.DateField(verbose_name='Data Sfarsit')
    campaign_active = models.BooleanField(default=False, verbose_name='Activ')
    product = models.ManyToManyField(Product)

    class Meta:
        ordering = ['campaign_name']

    def __str__(self):
        return self.campaign_name
