# Generated by Django 3.2 on 2021-06-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20210630_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
