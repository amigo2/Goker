# Generated by Django 2.1.4 on 2019-02-04 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20181207_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/%Y/%m/%d'),
        ),
    ]