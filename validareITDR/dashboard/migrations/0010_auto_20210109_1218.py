# Generated by Django 3.1.4 on 2021-01-09 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210109_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotionalcampaign',
            old_name='active_campaign',
            new_name='selected_campaign',
        ),
        migrations.AlterField(
            model_name='prize',
            name='promotional_campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.promotionalcampaign'),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotional_campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.promotionalcampaign'),
        ),
    ]
