# Generated by Django 2.0.4 on 2018-09-23 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_which_price_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='which_price_plan',
        ),
    ]
