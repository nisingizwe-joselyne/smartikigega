# Generated by Django 3.2 on 2021-05-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210512_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='recorder',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]