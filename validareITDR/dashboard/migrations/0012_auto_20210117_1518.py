# Generated by Django 3.1.4 on 2021-01-17 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210117_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotionalcampaign',
            name='prize',
        ),
        migrations.AddField(
            model_name='prize',
            name='promotional_campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.promotionalcampaign'),
        ),
    ]
