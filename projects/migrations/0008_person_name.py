# Generated by Django 2.0.4 on 2018-09-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180912_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='Esmaeel Komijani', max_length=500),
            preserve_default=False,
        ),
    ]
