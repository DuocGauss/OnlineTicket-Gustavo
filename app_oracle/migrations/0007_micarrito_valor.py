# Generated by Django 3.2.4 on 2021-07-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0006_micarrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='micarrito',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]