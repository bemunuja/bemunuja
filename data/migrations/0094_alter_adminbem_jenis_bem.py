# Generated by Django 3.2 on 2021-08-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0093_auto_20210809_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminbem',
            name='jenis_bem',
            field=models.CharField(blank=True, choices=[('BEM-UNUJA', 'BEM-UNUJA'), ('BEMF-teknik', 'BEMF-teknik'), ('BEMF-FAI', 'BEMF-FAI'), ('BEMF-KES', 'BEMF-KES'), ('BEMF-Soshum', 'BEMF-Soshum')], max_length=200, null=True),
        ),
    ]
