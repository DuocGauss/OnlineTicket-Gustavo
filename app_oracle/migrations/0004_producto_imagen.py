# Generated by Django 3.2.4 on 2021-06-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0003_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imgprod'),
        ),
    ]
