# Generated by Django 4.0.3 on 2023-09-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0011_remove_category_description_alter_product_hd_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
