# Generated by Django 4.2.15 on 2024-09-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0004_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='profile_list',
            field=models.CharField(default='None Assigned', max_length=255),
        ),
    ]
