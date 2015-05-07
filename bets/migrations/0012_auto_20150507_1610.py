# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0011_bet_expdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Player',
        ),
    ]
