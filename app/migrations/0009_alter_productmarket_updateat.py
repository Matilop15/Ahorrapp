# Generated by Django 4.0.5 on 2022-06-17 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_name_supermarket_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmarket',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 0, 48, 36, 383899)),
        ),
    ]