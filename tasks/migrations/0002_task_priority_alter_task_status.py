# Generated by Django 4.2.15 on 2024-08-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(1, 'LOW'), (2, 'MEDIUM'), (3, 'HIGH')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[(1, 'To-do'), (2, 'In Progress'), (3, 'Completed'), (4, 'Backlog')], default=1, max_length=15),
        ),
    ]
