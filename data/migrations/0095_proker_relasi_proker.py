# Generated by Django 3.2 on 2021-08-09 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0094_alter_adminbem_jenis_bem'),
    ]

    operations = [
        migrations.AddField(
            model_name='proker',
            name='relasi_proker',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
