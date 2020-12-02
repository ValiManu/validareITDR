# Generated by Django 3.1.4 on 2020-12-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name']},
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=50, verbose_name='Denumire')),
                ('campaign_start_date', models.DateField(verbose_name='Data Start')),
                ('campaign_end_date', models.DateField(verbose_name='Data Sfarsit')),
                ('campaign_active', models.BooleanField(default=False, verbose_name='Activ')),
                ('product', models.ManyToManyField(to='website.Product')),
            ],
        ),
    ]
