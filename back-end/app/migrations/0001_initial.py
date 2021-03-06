# Generated by Django 4.0.5 on 2022-06-18 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=120)),
                ('UrlImg', models.CharField(max_length=120)),
                ('Brand', models.CharField(max_length=120)),
                ('Slug', models.SlugField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SuperMarket',
            fields=[
                ('SuperMarketId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=120)),
                ('Address', models.CharField(max_length=120)),
                ('Phone', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('ProductMarketId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductPrice', models.CharField(max_length=45)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('SuperMarketId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supermarket')),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name': 'sub category',
                'verbose_name_plural': 'sub categories',
            },
        ),
        migrations.CreateModel(
            name='product_list',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('img_url', models.CharField(max_length=120)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sub_category')),
            ],
            options={
                'verbose_name': 'product list',
                'verbose_name_plural': 'product list',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('product_url', models.URLField()),
                ('update_date', models.DateField(auto_now=True)),
                ('market_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.market')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_list')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
