# Generated by Django 2.1.4 on 2019-05-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0007_auto_20190529_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adquisition',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='adquisition',
            old_name='end_time',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='end_time',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='recontact',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='recontact',
            old_name='end_time',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='salesevent',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='salesevent',
            old_name='end_time',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='adquisition',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='adquisition',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='news',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='news',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='recontact',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='recontact',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='salesevent',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='salesevent',
            name='start_time',
        ),
    ]
