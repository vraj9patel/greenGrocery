# Generated by Django 3.0.4 on 2020-03-13 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20200313_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
