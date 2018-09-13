from django.db import models
from team.models import TeamMate
# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=500)
    person = models.ForeignKey(TeamMate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    team_mates = models.ManyToManyField('Person', related_name='person_projects')
    technologies = models.ManyToManyField('Technology', related_name='tech_used_in_projects')
    customer = models.CharField(max_length=1500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)


class ProjectIntro(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title