# Generated by Django 3.1.4 on 2021-01-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_promotionalcampaign_prize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotionalcampaign',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='promotionalcampaign',
            name='product',
        ),
        migrations.AddField(
            model_name='prize',
            name='promotional_campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.promotionalcampaign'),
        ),
        migrations.AddField(
            model_name='product',
            name='promotional_campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.promotionalcampaign'),
        ),
    ]