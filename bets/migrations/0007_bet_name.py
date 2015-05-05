# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0006_bet_arbitrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
