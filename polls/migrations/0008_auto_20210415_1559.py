# Generated by Django 3.1.6 on 2021-04-15 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210414_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestrecord',
            name='farmercode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.regfarmer'),
        ),
    ]