from django.conf import settings
from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=30,)
    street = models.CharField(max_length=30,)
    street_no = models.IntegerField()

    def __str__(self):
        return self.city


class Shop(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    active_shop = models.BooleanField(default=True)
    network = models.ForeignKey('Network', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Network(models.Model):
    name = models.CharField(max_length=20)
    cif = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    url_img = models.CharField(max_length=200)
    active_product = models.BooleanField(default=True)
    promotional_campaign = models.ForeignKey('PromotionalCampaign', default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PromotionalCampaign(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    selected_campaign = models.BooleanField(default=False)
    shops_network = models.ForeignKey('Network', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Prize(models.Model):
    name = models.CharField(max_length=20)
    url_img = models.CharField(max_length=200)
    active_product = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    promotional_campaign = models.ForeignKey('PromotionalCampaign', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

