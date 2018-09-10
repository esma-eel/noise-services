from django.db import models
from markdown_deux import markdown
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image_slider = models.ImageField(upload_to='about/', blank=True, null=True)
    image_thumbnail = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_markdown(self):
        about_description = self.description
        return markdown(about_description) 
