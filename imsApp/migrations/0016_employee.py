# Generated by Django 4.0.3 on 2023-09-29 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0015_rename_employee_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('sec_name', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
