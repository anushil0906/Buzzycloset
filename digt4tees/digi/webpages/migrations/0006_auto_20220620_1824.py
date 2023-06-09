# Generated by Django 3.2.12 on 2022-06-20 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_remove_varient_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.subcategory', unique=True),
        ),
        migrations.AlterField(
            model_name='varient',
            name='color',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue')], default='', max_length=255),
        ),
    ]
