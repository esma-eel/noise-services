from django.db import models

# Create your models here.
class Testimonial(models.Model):
    from_who = models.CharField(max_length=250)
    job_title = models.CharField(max_length=1000)
    text = models.TextField()

    def __str__(self):
        return self.from_who


class TestimonialsIntro(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

