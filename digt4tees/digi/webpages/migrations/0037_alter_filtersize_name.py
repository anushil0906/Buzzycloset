# Generated by Django 3.2.14 on 2022-08-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0036_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtersize',
            name='name',
            field=models.CharField(choices=[('large', 'large'), ('medium', 'medium'), ('small', 'small'), ('topcenter', 'topcenter'), ('bottom', 'bottom'), ('bottomleft', 'bottomleft'), ('bottomright', 'bottomright')], default='', max_length=255),
        ),
    ]
