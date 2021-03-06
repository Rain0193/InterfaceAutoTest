# Generated by Django 2.1 on 2018-08-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=8, unique=True, verbose_name='用户名')),
                ('phone', models.CharField(max_length=11, verbose_name='联系手机号')),
                ('email', models.EmailField(max_length=11, verbose_name='邮箱')),
                ('role', models.IntegerField(null=True, verbose_name='用户角色')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息表',
                'db_table': 'userInfo',
            },
        ),
    ]
