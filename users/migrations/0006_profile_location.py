# Generated by Django 2.2.7 on 2020-05-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]