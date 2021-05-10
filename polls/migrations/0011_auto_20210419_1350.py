# Generated by Django 3.1.6 on 2021-04-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_cooperative_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allfarmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('harvesttype', models.CharField(max_length=255)),
                ('dateofbirth', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('Cooperative', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('cell', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='farmers',
            name='Cooperative',
            field=models.CharField(max_length=255),
        ),
    ]