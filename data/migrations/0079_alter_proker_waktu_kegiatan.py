# Generated by Django 3.2 on 2021-08-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0078_alter_proker_pencairan_proker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proker',
            name='waktu_kegiatan',
            field=models.DateField(blank=True, null=True),
        ),
    ]