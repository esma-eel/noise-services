from django.db import models
from django.urls import reverse
# Create your models here.

class SocialMediaItems(models.Model):
    name = models.CharField(max_length=500)
    team_mate = models.ForeignKey('TeamMate', on_delete=models.CASCADE, related_name='person_social_medias', null=True, blank=True)
    social_url = models.URLField()
    icon = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_name = models.CharField(max_length=1000)
    skill_level = models.IntegerField(blank=True, null=True)
    team_mate = models.ForeignKey('TeamMate', on_delete=models.CASCADE, related_name='person_skills', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skill_is_special = models.BooleanField(default=False)


    def __str__(self):
        return self.skill_name


class TeamMate(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    picture_small = models.ImageField(upload_to='team/small/')
    picture_big = models.ImageField(upload_to='team/big/')
    job_title = models.CharField(max_length=1000)
    contact_location = models.CharField(max_length=250)
    email = models.EmailField()
    website = models.URLField()


    def __str__(self):
        return self.name + ' ' + self.last_name

    
    def get_absolute_url(self):
        return reverse('team_mate', args=[self.id])


class TeamIntro(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title