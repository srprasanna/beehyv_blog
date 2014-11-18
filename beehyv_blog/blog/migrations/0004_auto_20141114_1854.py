# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141113_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags_list',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user_record',
            name='mobile',
            field=models.CharField(unique=True, max_length=10, verbose_name=b'Mobile(10 digits)'),
            preserve_default=True,
        ),
    ]
