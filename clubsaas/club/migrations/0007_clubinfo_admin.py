# Generated by Django 2.2.6 on 2021-06-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20210601_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubinfo',
            name='admin',
            field=models.CharField(default='admin', max_length=10, unique=True, verbose_name='username'),
        ),
    ]
