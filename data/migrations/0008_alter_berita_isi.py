# Generated by Django 3.2 on 2021-06-27 17:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_berita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='isi',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]