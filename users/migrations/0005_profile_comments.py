# Generated by Django 2.2.7 on 2020-05-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
