# Generated by Django 3.2.12 on 2022-06-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_rename_size_filtersize_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('large', 'large'), ('medium', 'medium'), ('small', 'small')], default='', max_length=255),
        ),
    ]
