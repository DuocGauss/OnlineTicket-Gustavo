# Generated by Django 3.2.4 on 2021-07-08 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0022_auto_20210707_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='idpedido',
            new_name='idpedidos',
        ),
    ]
