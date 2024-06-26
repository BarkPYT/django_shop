# Generated by Django 4.1.7 on 2023-03-19 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCShop', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PCShop.product')),
            ],
        ),
    ]
