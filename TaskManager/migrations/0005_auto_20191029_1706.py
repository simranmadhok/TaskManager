# Generated by Django 2.2.6 on 2019-10-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0004_auto_20191029_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='TaskManager.TaskComments'),
        ),
    ]
