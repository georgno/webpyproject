# Generated by Django 3.2.4 on 2021-07-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoebox', '0005_auto_20210708_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1),
        ),
    ]
