# Generated by Django 3.2 on 2021-08-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0086_berita_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminbem',
            name='telp_anggota',
            field=models.IntegerField(blank=True, default='628'),
        ),
    ]
