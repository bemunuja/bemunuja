# Generated by Django 3.2 on 2021-07-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_alter_bemf_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bemf',
            name='category',
            field=models.CharField(blank=True, choices=[('BEM fakultas teknik', 'BEM fakultas teknik'), ('BEM fakultas agama islam', 'BEM fakultas agama islam'), ('BEM fakultas kesehatan', 'BEM fakultas kesehatan'), ('BEM fakultas Soshum', 'BEM fakultas Soshum')], max_length=200, null=True),
        ),
    ]
