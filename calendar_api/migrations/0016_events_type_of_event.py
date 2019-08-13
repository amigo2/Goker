# Generated by Django 2.1.4 on 2019-06-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0015_auto_20190602_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='type_of_Event',
            field=models.CharField(choices=[('NO', 'news'), ('AD', 'adquisition'), ('RE', 're_contact'), ('CV', 'sales_e')], default='NO', max_length=2),
        ),
    ]
