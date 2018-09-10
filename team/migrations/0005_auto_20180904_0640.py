# Generated by Django 2.0.4 on 2018-09-04 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20180904_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='socialmediaitems',
            name='team_mate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_social_medias', to='team.TeamMate'),
        ),
    ]