# Generated by Django 3.2 on 2021-07-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0040_auto_20210728_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabellaporan',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tabelproposal',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
