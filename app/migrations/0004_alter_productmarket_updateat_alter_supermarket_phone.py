# Generated by Django 4.0.5 on 2022-06-16 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_productmarket_productname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmarket',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 20, 11, 16, 402201)),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='Phone',
            field=models.CharField(max_length=120),
        ),
    ]