# Generated by Django 3.2.12 on 2022-07-02 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0010_auto_20220702_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderphoto',
            old_name='lesson',
            new_name='order',
        ),
    ]
