# Generated by Django 3.2 on 2021-08-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0059_proker_ringkasan_anggaran'),
    ]

    operations = [
        migrations.AddField(
            model_name='proker',
            name='terbitan_sk',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
