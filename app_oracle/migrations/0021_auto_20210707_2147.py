# Generated by Django 3.2.4 on 2021-07-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0020_auto_20210707_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='idpedido',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]