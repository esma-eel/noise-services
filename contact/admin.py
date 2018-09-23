from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('name', 'email', 'phone' ,'message', 'file') #,'which_price_plan'


admin.site.register(Contact,ContactAdmin)
admin.site.register(ContactIntro)