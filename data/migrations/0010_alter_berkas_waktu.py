# Generated by Django 3.2 on 2021-06-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20210629_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berkas',
            name='waktu',
            field=models.DateField(blank=True, null=True),
        ),
    ]
