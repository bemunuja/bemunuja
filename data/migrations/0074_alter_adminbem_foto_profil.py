# Generated by Django 3.2 on 2021-08-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0073_auto_20210803_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminbem',
            name='foto_profil',
            field=models.ImageField(blank=True, default='logoadmin.png', upload_to=''),
        ),
    ]