# Generated by Django 3.1.4 on 2021-10-20 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_nmae',
            new_name='task_name',
        ),
    ]
