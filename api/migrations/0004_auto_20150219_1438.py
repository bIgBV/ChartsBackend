# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150219_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charts',
            old_name='data',
            new_name='jsonData',
        ),
        migrations.RemoveField(
            model_name='charts',
            name='name',
        ),
        migrations.AddField(
            model_name='charts',
            name='chartName',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='charts',
            name='isPrivate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='charts',
            name='description',
            field=models.CharField(default='', max_length=800, blank=True),
            preserve_default=True,
        ),
    ]
