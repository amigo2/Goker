# Generated by Django 2.1.4 on 2019-06-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0012_auto_20190602_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesevent',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesevent',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
