# Generated by Django 3.1.4 on 2020-12-02 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_store', models.CharField(max_length=20, verbose_name='Grup Magazin')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30, verbose_name='Denumire')),
                ('store_address', models.CharField(max_length=40, verbose_name='Adresa')),
                ('store_active', models.BooleanField(default=True, verbose_name='Activ')),
                ('group_store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.groupstore')),
            ],
            options={
                'ordering': ['store_name'],
            },
        ),
    ]
