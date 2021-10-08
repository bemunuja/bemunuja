# Generated by Django 3.2 on 2021-07-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_remove_berkas_kegiatan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bemf',
            old_name='phone',
            new_name='jabatan',
        ),
        migrations.RenameField(
            model_name='bemu',
            old_name='phone',
            new_name='jabatan',
        ),
        migrations.AddField(
            model_name='bemf',
            name='nim',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bemu',
            name='nim',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
