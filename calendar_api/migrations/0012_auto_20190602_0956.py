# Generated by Django 2.1.4 on 2019-06-02 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0011_auto_20190602_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesevent',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='salesevent',
            name='start_date',
        ),
    ]
