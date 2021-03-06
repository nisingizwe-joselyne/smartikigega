# Generated by Django 3.2 on 2021-05-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210514_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='loan_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='recorder',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='loan',
            name='firstname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='telephone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
