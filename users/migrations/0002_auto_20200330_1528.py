# Generated by Django 2.2.7 on 2020-03-30 15:28

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
