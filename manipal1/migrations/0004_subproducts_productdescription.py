# Generated by Django 4.1.3 on 2022-11-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manipal1', '0003_subproducts_alter_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproducts',
            name='productdescription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
