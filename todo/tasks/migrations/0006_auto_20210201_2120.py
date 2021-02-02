# Generated by Django 3.1.6 on 2021-02-01 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BinaryField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
