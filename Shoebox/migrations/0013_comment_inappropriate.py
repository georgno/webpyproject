# Generated by Django 3.2.4 on 2021-07-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoebox', '0012_auto_20210714_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='inappropriate',
            field=models.BooleanField(default=False),
        ),
    ]
