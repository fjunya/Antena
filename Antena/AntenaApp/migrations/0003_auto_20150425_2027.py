# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AntenaApp', '0002_auto_20150425_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8e\xb2\xe8\xbc\x89\xe6\x97\xa5', null=True),
            preserve_default=True,
        ),
    ]
