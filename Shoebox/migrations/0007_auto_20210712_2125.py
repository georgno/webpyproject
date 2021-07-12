# Generated by Django 3.2.4 on 2021-07-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoebox', '0006_comment_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='book',
            new_name='box',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='5'),
        ),
    ]
