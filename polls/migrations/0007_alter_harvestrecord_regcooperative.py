# Generated by Django 3.2 on 2021-05-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_harvestrecord_recorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestrecord',
            name='regCooperative',
            field=models.CharField(max_length=255),
        ),
    ]
