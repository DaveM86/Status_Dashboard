# Generated by Django 3.2.7 on 2021-10-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_task_day_of_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='day_of_task',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
