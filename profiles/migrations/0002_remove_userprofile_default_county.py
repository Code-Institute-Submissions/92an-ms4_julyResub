# Generated by Django 3.1.7 on 2021-07-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_county',
        ),
    ]
