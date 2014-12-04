# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(primary_key=True, serialize=False, max_length=75)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', verbose_name='groups', blank=True, to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', blank=True, to='auth.Permission', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
