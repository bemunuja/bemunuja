# Generated by Django 3.2 on 2021-07-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_berita_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='deskripsi',
            field=models.CharField(blank=True, max_length=132, null=True),
        ),
    ]
