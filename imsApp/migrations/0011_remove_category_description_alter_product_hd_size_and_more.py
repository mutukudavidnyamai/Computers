# Generated by Django 4.0.3 on 2023-09-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0010_alter_product_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='hd_size',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(choices=[('1', 'HP'), ('2', 'DELL')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(choices=[('1', '2GB'), ('2', '4GB')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='serial',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
