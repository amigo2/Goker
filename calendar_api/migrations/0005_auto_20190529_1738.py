# Generated by Django 2.1.4 on 2019-05-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0004_auto_20190529_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adquisition',
            name='adquisition_name',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_name',
        ),
        migrations.RemoveField(
            model_name='recontact',
            name='recontact_name',
        ),
        migrations.RemoveField(
            model_name='salesevent',
            name='sales_event_name',
        ),
        migrations.AddField(
            model_name='adquisition',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recontact',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesevent',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='address',
            field=models.CharField(blank=True, default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='description',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='end_date',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='end_time',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='start_date',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adquisition',
            name='start_time',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='address',
            field=models.CharField(blank=True, default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='end_date',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='end_time',
            field=models.CharField(default=11, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='start_date',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='start_time',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recontact',
            name='address',
            field=models.CharField(blank=True, default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recontact',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recontact',
            name='end_date',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='recontact',
            name='end_time',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='recontact',
            name='start_date',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='recontact',
            name='start_time',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='end_date',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='end_time',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='start_date',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='salesevent',
            name='start_time',
            field=models.CharField(max_length=4),
        ),
    ]