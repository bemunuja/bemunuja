# Generated by Django 3.2 on 2021-08-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0085_tabellaporan_waktu_pengumpulan'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
