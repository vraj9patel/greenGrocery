# Generated by Django 3.0.4 on 2020-03-13 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200312_1823'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0009_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
