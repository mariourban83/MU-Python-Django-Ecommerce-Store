# Generated by Django 3.0.4 on 2020-03-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(),
        ),
    ]
