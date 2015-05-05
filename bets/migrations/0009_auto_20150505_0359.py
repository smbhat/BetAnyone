# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0008_auto_20150505_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='bets.User'),
        ),
    ]
