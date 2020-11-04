# Generated by Django 3.1 on 2020-10-22 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='未定义', max_length=30, unique=True, verbose_name='分类名称')),
            ],
            options={
                'verbose_name_plural': '分类',
                'db_table': 't_catagory',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(default='未定义', max_length=30, unique=True, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 't_tag',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=300, verbose_name='描述')),
                ('content', models.TextField(verbose_name='内容')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modifytime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.catagorymodel', verbose_name='分类')),
                ('tag', models.ManyToManyField(to='blog.TagModel', verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '文章',
                'db_table': 't_article',
            },
        ),
    ]
