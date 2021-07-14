# Generated by Django 3.2.4 on 2021-07-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoebox', '0006_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5'),
        ),
    ]