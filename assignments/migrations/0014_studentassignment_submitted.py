# Generated by Django 3.1.4 on 2021-04-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0013_assignment_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
