# Generated by Django 4.1.3 on 2022-12-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manipal1', '0008_ord_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
