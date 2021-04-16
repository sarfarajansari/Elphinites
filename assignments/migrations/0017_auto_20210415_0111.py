# Generated by Django 3.1.4 on 2021-04-14 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0016_auto_20210415_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='duedate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentassignment',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentassignment', to='assignments.assignment'),
        ),
        migrations.AlterField(
            model_name='studentassignment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='assignments.student'),
        ),
    ]
