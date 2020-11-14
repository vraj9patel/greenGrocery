# Generated by Django 3.0.4 on 2020-03-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200307_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('V', 'Vegetables'), ('F', 'Fruits')], default='V', max_length=1),
        ),
    ]
