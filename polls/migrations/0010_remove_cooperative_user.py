# Generated by Django 3.1.6 on 2021-04-17 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210416_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooperative',
            name='user',
        ),
    ]