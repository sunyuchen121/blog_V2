# Generated by Django 3.0.8 on 2022-03-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_util', '0002_operaterecord_operate'),
    ]

    operations = [
        migrations.AddField(
            model_name='operaterecord',
            name='editList',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='operaterecord',
            name='operate',
            field=models.CharField(choices=[('新增', '新增'), ('修改', '修改'), ('删除', '删除'), ('history', 'history')], default='history', max_length=16),
        ),
    ]
