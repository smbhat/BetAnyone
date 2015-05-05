# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='taker',
            field=models.ForeignKey(related_name='taker', default=0, to='bets.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='creater',
            field=models.ForeignKey(related_name='creater', to='bets.User'),
            preserve_default=True,
        ),
    ]
