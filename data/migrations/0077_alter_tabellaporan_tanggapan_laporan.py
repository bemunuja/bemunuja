# Generated by Django 3.2 on 2021-08-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0076_auto_20210803_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabellaporan',
            name='tanggapan_laporan',
            field=models.CharField(blank=True, choices=[('masih diperika', 'masih diperika'), ('AJUKAN ULANG', 'AJUKAN ULANG'), ('DITOLAK', 'DITOLAK'), ('DITERIMA', 'DITERIMA')], default='belum diperiksa', max_length=200),
        ),
    ]
