# Generated by Django 4.1.3 on 2022-12-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manipal1', '0007_ord'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
