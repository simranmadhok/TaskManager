# Generated by Django 2.2.6 on 2019-10-29 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0006_auto_20191029_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomments',
            name='ckpt_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
