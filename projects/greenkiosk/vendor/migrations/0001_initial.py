# Generated by Django 4.2.3 on 2023-07-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
                ('shop_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=32)),
            ],
        ),
    ]
