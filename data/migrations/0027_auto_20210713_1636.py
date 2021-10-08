# Generated by Django 3.2 on 2021-07-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0026_alter_berita_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='berkas',
            name='catatan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='berkas',
            name='notifikasi',
            field=models.CharField(blank=True, choices=[('diterima', 'diterima'), ('ditolak', 'ditolak')], max_length=200, null=True),
        ),
    ]
