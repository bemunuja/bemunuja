# Generated by Django 3.2 on 2021-07-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_alter_bemf_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='berkas',
            name='waktu',
        ),
    ]
