# Generated by Django 3.2.14 on 2022-08-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0037_alter_filtersize_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('large', 'large'), ('medium', 'medium'), ('small', 'small'), ('topcenter', 'topcenter'), ('bottom', 'bottom'), ('bottomleft', 'bottomleft'), ('bottomright', 'bottomright')], default='large', max_length=255),
        ),
    ]
