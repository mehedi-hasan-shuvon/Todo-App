# Generated by Django 3.1.5 on 2021-02-04 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
