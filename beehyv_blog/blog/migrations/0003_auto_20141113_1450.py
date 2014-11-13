# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20141110_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_record',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RenameField(
            model_name='blogpost_record',
            old_name='blogPost_id',
            new_name='blog_post_id',
        ),
        migrations.RenameField(
            model_name='user_record',
            old_name='is_active',
            new_name='is_email_verified',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='created_date_time',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_record',
            name='username',
        ),
        migrations.AddField(
            model_name='user_record',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
