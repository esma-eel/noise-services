from django.contrib import admin
from .models import *
# Register your models here.

class TeamMateAdmin(admin.ModelAdmin):
    # filter_horizontal = ('skills', 'social_media',)
    pass

admin.site.register(TeamIntro)
admin.site.register(TeamMate,TeamMateAdmin)
admin.site.register(Skill)
admin.site.register(SocialMediaItems)
