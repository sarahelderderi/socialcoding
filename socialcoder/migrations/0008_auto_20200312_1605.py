# Generated by Django 2.2.7 on 2020-03-12 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialcoder', '0007_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='clique',
        ),
    ]