# Generated by Django 3.0.8 on 2020-09-14 03:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('create', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '日记',
                'verbose_name_plural': '日记',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('about', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('img', models.URLField(default='https://www.yanshisan.cn/logo.png')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['create'],
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('usertype', models.CharField(choices=[('1000', '会员'), ('1', '超级管理员'), ('100', '管理员')], default='会员', max_length=32)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', ckeditor.fields.RichTextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(choices=[('个人日记', '个人日记'), ('python', 'python'), ('django', 'django')], default='python', max_length=32)),
                ('state', models.CharField(choices=[('转载', '转载'), ('原创', '原创')], default='原创', max_length=32)),
                ('read', models.IntegerField(default=0)),
                ('picture_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='article_img')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '博文管理',
                'verbose_name_plural': '博文管理',
                'ordering': ['-create'],
            },
        ),
    ]
