# Generated by Django 3.1.4 on 2021-04-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0008_auto_20210412_2243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
