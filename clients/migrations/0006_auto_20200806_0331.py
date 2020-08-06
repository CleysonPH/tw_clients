# Generated by Django 2.2.13 on 2020-08-06 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20200806_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pedido Realizado'), ('F', 'Fazendo'), ('E', 'Saiu para entrega')], max_length=1, verbose_name='Status'),
        ),
    ]