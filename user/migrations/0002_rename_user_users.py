# Generated by Django 3.2.6 on 2021-08-12 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0011_auto_20210812_0305'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
