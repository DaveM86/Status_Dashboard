# Generated by Django 3.2.7 on 2021-10-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_remove_task_day_of_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='day_of_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.daysoftheweek'),
        ),
    ]
