# Generated by Django 3.2 on 2021-05-31 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_loan_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestrecord',
            name='recorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.recorder'),
        ),
    ]