# Generated by Django 4.0.3 on 2023-09-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0014_rename_category_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Category',
        ),
    ]