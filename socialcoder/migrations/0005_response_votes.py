# Generated by Django 2.2.7 on 2020-02-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcoder', '0004_vote_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]