# Generated by Django 3.2.4 on 2021-07-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0011_auto_20210707_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='rut',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]