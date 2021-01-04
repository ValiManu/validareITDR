from django.db import models


class Sales (models.Model):
    ticket_no = models.IntegerField()
    ticket_date = models.DateTimeField(verbose_name='Data Bon')
    shop = models.ForeignKey('dashboard.Shop', on_delete=models.SET_NULL, null=True)
    prize = models.ForeignKey('dashboard.Prize', on_delete=models.SET_NULL, null=True)
    total_sale = models.IntegerField(default=0)


class ProductsSold (models.Model):
    sale = models.ForeignKey('Sales', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('dashboard.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
