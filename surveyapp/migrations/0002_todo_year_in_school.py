# Generated by Django 3.2.10 on 2021-12-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
