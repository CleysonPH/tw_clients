# Generated by Django 2.2.13 on 2020-08-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200, verbose_name='Rua')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('complement', models.CharField(max_length=200, verbose_name='Complemento')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
