# Generated by Django 3.2.7 on 2021-09-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_deployment'),
    ]

    operations = [
        migrations.AddField(
            model_name='smt',
            name='day_of_weekly',
            field=models.CharField(default='Monday', max_length=10),
            preserve_default=False,
        ),
    ]
