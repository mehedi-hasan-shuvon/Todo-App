# Generated by Django 3.1.5 on 2021-02-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_posted',
        ),
    ]
