# Generated by Django 3.2 on 2021-08-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0071_auto_20210803_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proker',
            name='proposal_kegiatan',
            field=models.FileField(blank=True, default='tidak ada berkas', upload_to=''),
        ),
        migrations.AlterField(
            model_name='proker',
            name='struktur_kepanitiaan',
            field=models.FileField(blank=True, default='tidak ada berkas', upload_to=''),
        ),
        migrations.AlterField(
            model_name='proker',
            name='tanggapan_proker',
            field=models.CharField(blank=True, choices=[('masih diperika', 'masih diperika'), ('DITERIMA', 'DITERIMA'), ('DITOLAK', 'DITOLAK')], default='belum diperiksa3', max_length=200),
        ),
    ]
