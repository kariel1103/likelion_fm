# Generated by Django 3.2.6 on 2021-08-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, unique=True, verbose_name='id')),
                ('user_pw', models.CharField(max_length=100, verbose_name='password')),
                ('user_name', models.CharField(max_length=20, unique=True, verbose_name='name')),
                ('user_email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user',
            },
        ),
    ]