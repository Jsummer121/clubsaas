# Generated by Django 2.2.6 on 2021-06-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20210601_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubadmin',
            name='depart',
            field=models.CharField(default='all', max_length=10, verbose_name='depart'),
        ),
        migrations.AlterField(
            model_name='deliveried',
            name='final',
            field=models.IntegerField(choices=[(2, '通过'), (1, '进行中'), (3, '淘汰')], verbose_name='final'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.IntegerField(choices=[(2, '女'), (1, '男')], verbose_name='gender'),
        ),
    ]
