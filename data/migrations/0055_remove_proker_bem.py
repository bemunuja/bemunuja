# Generated by Django 3.2 on 2021-08-02 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0054_proker_id_adminbem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proker',
            name='bem',
        ),
    ]
