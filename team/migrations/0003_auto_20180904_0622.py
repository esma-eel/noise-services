# Generated by Django 2.0.4 on 2018-09-04 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_teammate_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='person',
        ),
        migrations.RemoveField(
            model_name='socialmediaitems',
            name='person',
        ),
        migrations.RemoveField(
            model_name='teammate',
            name='skills',
        ),
        migrations.AddField(
            model_name='teammate',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_mate', to='team.Skill'),
        ),
        migrations.RemoveField(
            model_name='teammate',
            name='social_media',
        ),
        migrations.AddField(
            model_name='teammate',
            name='social_media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_mate', to='team.SocialMediaItems'),
        ),
    ]
