# Generated by Django 2.0.4 on 2018-09-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20180912_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='which_price_plan',
            field=models.CharField(choices=[('هیچکدام', 'هیچکدام'), ('پایه', 'پایه'), ('حرفه ای', 'حرفه ای'), ('پیشرفته', 'پیشرفته'), ('خیلی پیشرفته', 'خیلی پیشرفته'), ('سوپر پیشرفته', 'سوپر پیشرفته')], default='هیچکدام', max_length=500),
        ),
    ]
