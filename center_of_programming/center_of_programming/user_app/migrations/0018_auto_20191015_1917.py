# Generated by Django 2.2.3 on 2019-10-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0017_auto_20191015_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(default=0, max_length=11),
        ),
    ]
