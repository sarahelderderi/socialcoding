# Generated by Django 2.2.7 on 2020-03-14 21:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialcoder', '0022_auto_20200314_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code_snippet',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
