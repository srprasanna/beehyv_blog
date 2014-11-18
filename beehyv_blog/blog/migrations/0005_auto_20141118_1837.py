# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141114_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost_record',
            name='content',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
