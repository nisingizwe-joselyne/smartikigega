# Generated by Django 3.2 on 2021-06-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_alter_harvestrecord_recorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestrecord',
            name='recorder',
            field=models.CharField(max_length=255),
        ),
    ]
