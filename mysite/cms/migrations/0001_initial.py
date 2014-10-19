# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u66f8\u7c4d\u540d')),
                ('publisher', models.CharField(max_length=255, verbose_name='\u51fa\u7248\u793e', blank=True)),
                ('page', models.IntegerField(default=0, verbose_name='\u30da\u30fc\u30b8\u6570', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='\u30b3\u30e1\u30f3\u30c8', blank=True)),
                ('book', models.ForeignKey(related_name='impressions', verbose_name='\u66f8\u7c4d', to='cms.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
