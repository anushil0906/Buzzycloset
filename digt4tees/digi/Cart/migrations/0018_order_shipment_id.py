# Generated by Django 3.2.14 on 2022-08-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0017_shipauthtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipment_id',
            field=models.CharField(default='', max_length=15),
        ),
    ]
