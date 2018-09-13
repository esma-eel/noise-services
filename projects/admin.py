from django.contrib import admin
from .models import *
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('team_mates', 'technologies',)


admin.site.register(ProjectIntro)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
admin.site.register(Person)
