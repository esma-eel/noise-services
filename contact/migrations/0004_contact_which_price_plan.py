# Generated by Django 2.0.4 on 2018-09-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_which_price_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='which_price_plan',
            field=models.CharField(choices=[('هیچکدام', 'هیچکدام')], default='هیچکدام', max_length=500),
        ),
    ]
