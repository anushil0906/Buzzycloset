# Generated by Django 3.2.12 on 2022-06-25 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0006_order_made_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
