# Generated by Django 3.2.4 on 2021-07-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0010_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='idpedido',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
