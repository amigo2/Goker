# Generated by Django 2.1.4 on 2018-12-07 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='reference',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
