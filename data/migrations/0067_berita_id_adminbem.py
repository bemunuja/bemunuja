# Generated by Django 3.2 on 2021-08-02 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0066_alter_proker_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='id_Adminbem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.adminbem'),
        ),
    ]
