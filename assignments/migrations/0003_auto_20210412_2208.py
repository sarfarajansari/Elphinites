# Generated by Django 3.1.4 on 2021-04-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
