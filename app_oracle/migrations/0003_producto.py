# Generated by Django 3.2.4 on 2021-06-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0002_auto_20210618_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=50)),
                ('valor', models.IntegerField(default=0)),
                ('stock', models.CharField(max_length=25)),
            ],
        ),
    ]
