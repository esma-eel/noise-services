# Generated by Django 2.0.4 on 2018-09-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammate',
            name='description',
            field=models.TextField(default='لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه'),
            preserve_default=False,
        ),
    ]
