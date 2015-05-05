# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0004_auto_20150505_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='taker',
            field=models.ForeignKey(related_name='taker', default=0, to='bets.User'),
        ),
    ]
