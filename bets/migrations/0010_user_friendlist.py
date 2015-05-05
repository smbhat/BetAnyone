# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0009_auto_20150505_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friendlist',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
