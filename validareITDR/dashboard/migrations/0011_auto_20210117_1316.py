# Generated by Django 3.1.4 on 2021-01-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210109_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='promotional_campaign',
        ),
        migrations.RemoveField(
            model_name='product',
            name='promotional_campaign',
        ),
        migrations.AddField(
            model_name='promotionalcampaign',
            name='prize',
            field=models.ManyToManyField(to='dashboard.Prize'),
        ),
        migrations.AddField(
            model_name='promotionalcampaign',
            name='product',
            field=models.ManyToManyField(to='dashboard.Product'),
        ),
    ]