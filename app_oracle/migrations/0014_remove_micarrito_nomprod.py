# Generated by Django 3.2.4 on 2021-07-07 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0013_micarrito_nomprod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='micarrito',
            name='nomprod',
        ),
    ]
