# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150217_0807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charts',
            options={'ordering': ('createdOn',)},
        ),
        migrations.AddField(
            model_name='charts',
            name='createdOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
