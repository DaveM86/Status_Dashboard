# Generated by Django 3.2.7 on 2021-09-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_softwareupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('location_code', models.CharField(max_length=5)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
