# Generated by Django 3.2.9 on 2021-11-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eServiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropinsmodel',
            name='device_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
