# Generated by Django 3.2.12 on 2022-06-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0016_auto_20220621_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_customize',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id_char', models.CharField(default='', max_length=255)),
                ('timage1', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('timage2', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('timage3', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('image1', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('image2', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('image3', models.ImageField(null=True, upload_to='media/customtees/%y/%m/')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('user', models.CharField(default='', max_length=200)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('payment_status', models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING'), (4, 'PENDING CASH'), (5, 'Order cancelled and refund processed')], default=3)),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
