# Generated by Django 3.2 on 2021-09-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0105_sk_periode'),
    ]

    operations = [
        migrations.CreateModel(
            name='aspirasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identitas', models.CharField(blank=True, default='Identitas-mu', max_length=15)),
                ('komentar', models.CharField(blank=True, default='Isi disini', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'aspirasi',
            },
        ),
    ]
