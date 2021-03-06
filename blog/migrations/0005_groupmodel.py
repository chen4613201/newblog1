# Generated by Django 3.1.3 on 2020-11-11 11:52

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0004_delete_groupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('is_cust_group', models.BooleanField()),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组',
                'db_table': 't_group',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
