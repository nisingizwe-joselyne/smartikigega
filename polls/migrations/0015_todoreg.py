# Generated by Django 3.2 on 2021-05-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20210521_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todoreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
            ],
        ),
    ]
