# Generated by Django 3.2.6 on 2021-08-12 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0010_alter_community_writer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': '게시판', 'verbose_name_plural': '게시판'},
        ),
        migrations.AlterModelTable(
            name='community',
            table='board',
        ),
    ]
