# Generated by Django 3.1 on 2020-10-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(default='未定义', max_length=10, unique=True, verbose_name='菜单名')),
                ('murl', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '菜单',
                'db_table': 't_menu',
            },
        ),
    ]