# Generated by Django 2.2.7 on 2020-03-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcoder', '0006_responsevote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]