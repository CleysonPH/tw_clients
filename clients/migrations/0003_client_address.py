# Generated by Django 2.2.13 on 2020-08-05 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.Address', verbose_name='Endereço'),
        ),
    ]
