# Generated by Django 3.2.4 on 2021-07-07 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0008_micarrito_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='micarrito',
            name='descripcion',
        ),
    ]
