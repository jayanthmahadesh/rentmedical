# Generated by Django 4.1.3 on 2022-11-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manipal1', '0004_subproducts_productdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproducts',
            name='productimage',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
