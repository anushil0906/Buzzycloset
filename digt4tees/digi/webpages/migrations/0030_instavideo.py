# Generated by Django 3.2.14 on 2022-08-05 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0029_happycustomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstaVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_video', models.FileField(null=True, upload_to='instavideos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'mp3'])])),
            ],
        ),
    ]
