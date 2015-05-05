# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0007_bet_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='creater',
        ),
        migrations.AddField(
            model_name='bet',
            name='creator',
            field=models.ForeignKey(related_name='creator', default=0, to='bets.User'),
        ),
    ]
