# Generated by Django 3.2 on 2021-08-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0084_alter_proker_waktu_kegiatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabellaporan',
            name='waktu_pengumpulan',
            field=models.DateField(blank=True, null=True),
        ),
    ]
