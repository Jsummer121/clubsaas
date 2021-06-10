# Generated by Django 2.2.6 on 2021-06-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('token', models.CharField(max_length=128, unique=True)),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='username')),
            ],
        ),
        migrations.CreateModel(
            name='studentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('openid', models.CharField(max_length=30, unique=True, verbose_name='openid')),
                ('resumeid', models.SmallIntegerField(verbose_name='resumeid')),
            ],
            options={
                'index_together': {('openid', 'resumeid')},
            },
        ),
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=5, verbose_name='name')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='gender')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='phone')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email')),
                ('qq', models.CharField(max_length=10, unique=True, verbose_name='qq')),
                ('profile', models.CharField(max_length=300, verbose_name='profile')),
                ('photo', models.URLField(verbose_name='photo')),
                ('college', models.CharField(max_length=10)),
                ('stuid', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('id', 'phone', 'qq', 'email')},
            },
        ),
        migrations.CreateModel(
            name='deliveried',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('clubid', models.SmallIntegerField(verbose_name='clubid')),
                ('departOne', models.CharField(max_length=10)),
                ('departTwo', models.CharField(max_length=10)),
                ('resumeid', models.SmallIntegerField(verbose_name='resumeid')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('current', models.SmallIntegerField(verbose_name='current')),
                ('final', models.IntegerField(choices=[(2, '通过'), (3, '淘汰'), (1, '进行中')], verbose_name='final')),
            ],
            options={
                'unique_together': {('clubid', 'resumeid', 'current')},
            },
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='name')),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='clubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=5, verbose_name='name')),
                ('logo', models.URLField(verbose_name='logo')),
                ('departments', models.CharField(max_length=50, verbose_name='departments')),
                ('belong', models.CharField(max_length=10, verbose_name='belong')),
                ('detail', models.CharField(max_length=1000, verbose_name='detail')),
                ('pic1', models.URLField(verbose_name='pic1')),
                ('pic2', models.URLField(verbose_name='pic2')),
                ('pic3', models.URLField(verbose_name='pic3')),
                ('pic4', models.URLField(verbose_name='pic4')),
            ],
            options={
                'unique_together': {('belong', 'name')},
            },
        ),
        migrations.CreateModel(
            name='clubAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('level', models.SmallIntegerField(verbose_name='level')),
                ('ownerClubId', models.SmallIntegerField(null=True)),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='username')),
                ('pwd', models.CharField(max_length=32, verbose_name='password')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email')),
            ],
            options={
                'unique_together': {('username', 'email')},
            },
        ),
    ]
