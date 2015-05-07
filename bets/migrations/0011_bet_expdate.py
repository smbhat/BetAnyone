# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0010_user_friendlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='expdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
