# Generated by Django 3.1.4 on 2021-04-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0009_auto_20210412_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assignments.studentassignment')),
            ],
        ),
    ]
