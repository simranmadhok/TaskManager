# Generated by Django 2.2.6 on 2019-10-29 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0003_taskcomments_ckpt_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date_due'], 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='taskcomments',
            options={'verbose_name_plural': 'Task Comments'},
        ),
    ]
