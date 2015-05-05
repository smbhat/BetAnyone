# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_bet_arbitrator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='arbitrator',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='taker',
        ),
    ]
