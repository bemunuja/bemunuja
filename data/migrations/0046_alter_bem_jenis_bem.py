# Generated by Django 3.2 on 2021-07-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0045_alter_bem_jenis_bem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bem',
            name='jenis_bem',
            field=models.CharField(blank=True, choices=[('BEM-UNUJA', 'BEM-UNUJA'), ('BEMF-teknik', 'BEMF-teknik'), ('BEMF-FAI', 'BEMF-FAI'), ('BEMF-KES', 'BEMF-KES'), ('BEMF-Soshum', 'BEMF-Soshum')], max_length=200, null=True),
        ),
    ]
