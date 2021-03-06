# Generated by Django 3.2 on 2021-12-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0006_remove_todo_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='datecompleted',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='important',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='ambient',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='ergonomic',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='individual',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='infrastructure',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='learningactivity',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='learningmode',
            field=models.CharField(default='formal', max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='people',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='rules',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='spatial',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='todo',
            name='virtual',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
