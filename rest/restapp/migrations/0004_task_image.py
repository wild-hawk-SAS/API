# Generated by Django 3.1.4 on 2021-10-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
