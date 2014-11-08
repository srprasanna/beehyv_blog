# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost_record',
            fields=[
                ('blogPost_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('total_views', models.IntegerField()),
                ('visibility', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment_record',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('visibility', models.BooleanField(default=True)),
                ('blog_post_id', models.ForeignKey(to='blog.BlogPost_record')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Liked_post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_post_id', models.ForeignKey(to='blog.BlogPost_record')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags_list',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('tag_name', models.CharField(max_length=50)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('parent_id', models.IntegerField()),
                ('root_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_record',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(unique=True, max_length=20, editable=False)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=50, editable=False)),
                ('mobile', models.CharField(unique=True, max_length=10)),
                ('designation', models.CharField(max_length=20)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_id', models.ForeignKey(to='blog.Tags_list')),
                ('user_id', models.ForeignKey(to='blog.User_record')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tags_list',
            name='user_id',
            field=models.ForeignKey(to='blog.User_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liked_post',
            name='user_id',
            field=models.ForeignKey(to='blog.User_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment_record',
            name='user_id',
            field=models.ForeignKey(to='blog.User_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost_record',
            name='user_id',
            field=models.ForeignKey(to='blog.User_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog_tags',
            name='blog_post_id',
            field=models.ForeignKey(to='blog.BlogPost_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog_tags',
            name='tag_id',
            field=models.ForeignKey(to='blog.Tags_list'),
            preserve_default=True,
        ),
    ]
