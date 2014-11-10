# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost_record',
            name='content',
            field=models.CharField(max_length=50000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost_record',
            name='slug',
            field=models.SlugField(default=b'', unique=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost_record',
            name='total_views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment_record',
            name='comment',
            field=models.CharField(max_length=50000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_record',
            name='designation',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_record',
            name='email',
            field=models.EmailField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_record',
            name='first_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_record',
            name='last_name',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_record',
            name='username',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
