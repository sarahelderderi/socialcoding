# Generated by Django 2.2.7 on 2020-04-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcoder', '0034_auto_20200417_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='best',
            field=models.BooleanField(default=False),
        ),
    ]
