from django.conf import settings
from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=30, verbose_name='Oras')
    street = models.CharField(max_length=30, verbose_name='Strada')
    street_no = models.IntegerField(verbose_name='Nr.')

    def __str__(self):
        return self.city


class Shop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nume Magazin')
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    active_shop = models.BooleanField(verbose_name='Activ', default=True)
    network = models.ForeignKey('Network', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Network(models.Model):
    name = models.CharField(max_length=20, verbose_name='Retea')
    cif = models.IntegerField(verbose_name='CUI')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nume Produs')
    url_img = models.CharField(max_length=200, verbose_name='URL Img')
    active_product = models.BooleanField(verbose_name='Activ', default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PromotionalCampaign(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nume Campanie')
    start_date = models.DateField(verbose_name='Data Start')
    end_date = models.DateField(verbose_name='Data Sfarsit')
    active_campaign = models.BooleanField(default=False, verbose_name='Activ')
    product = models.ManyToManyField('Product')
    shops_network = models.ForeignKey('Network', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Prize(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nume Premiu')
    url_img = models.CharField(max_length=200, verbose_name='URL Img')
    active_product = models.BooleanField(verbose_name='Activ', default=True)
    quantity = models.IntegerField(default=0, verbose_name='Stoc')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)

    def __str__(self):
        return self.name

