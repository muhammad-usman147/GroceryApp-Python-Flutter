# Generated by Django 3.2.4 on 2021-06-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartsystem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
