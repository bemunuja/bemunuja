# Generated by Django 3.2 on 2021-06-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_berkas_waktu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berkas',
            name='waktu',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]