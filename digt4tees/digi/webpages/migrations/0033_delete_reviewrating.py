# Generated by Django 3.2.14 on 2022-08-06 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0032_remove_reviewrating_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewRating',
        ),
    ]
