# Generated by Django 3.2 on 2021-08-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0062_auto_20210802_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proker',
            options={'verbose_name_plural': 'proker'},
        ),
        migrations.AddField(
            model_name='adminbem',
            name='no_rekening',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adminbem',
            name='telp_anggota',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]