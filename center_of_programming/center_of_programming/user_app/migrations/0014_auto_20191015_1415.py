# Generated by Django 2.2.3 on 2019-10-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0013_auto_20191015_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
