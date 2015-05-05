# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0005_bet_taker'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='arbitrator',
            field=models.ForeignKey(related_name='arbitrator', default=0, to='bets.User'),
        ),
    ]
