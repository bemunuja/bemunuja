# Generated by Django 3.2 on 2021-06-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210617_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='berkas',
            name='berkas',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
