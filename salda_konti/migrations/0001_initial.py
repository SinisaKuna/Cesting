# Generated by Django 4.1.3 on 2022-11-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaldaKonti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konto', models.TextField(blank=True, max_length=100)),
                ('naziv', models.TextField(blank=True, max_length=100)),
                ('duguje', models.TextField(blank=True, max_length=100)),
                ('potrazuje', models.TextField(blank=True, max_length=100)),
                ('saldo', models.TextField(blank=True, max_length=100)),
                ('dug', models.FloatField()),
                ('pot', models.FloatField()),
                ('sal', models.FloatField()),
            ],
        ),
    ]
