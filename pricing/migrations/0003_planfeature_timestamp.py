# Generated by Django 2.0.4 on 2018-09-25 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_auto_20180925_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='planfeature',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 9, 25, 4, 30, 11, 296921, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
