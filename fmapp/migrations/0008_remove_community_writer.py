# Generated by Django 3.2.5 on 2021-08-11 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0007_community_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='writer',
        ),
    ]