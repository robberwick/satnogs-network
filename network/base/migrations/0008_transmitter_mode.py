# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150814_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmitter',
            name='mode',
            field=models.ForeignKey(related_name='transmitters', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='base.Mode', null=True),
        ),
    ]
