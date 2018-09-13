from django.contrib import admin
from .models import Testimonial, TestimonialsIntro
# Register your models here.
class TestimonialsIntroAdmin(admin.ModelAdmin):
    list_display = ('title', 'description' ,'active',)
    list_editable = ('active',)


admin.site.register(Testimonial)
admin.site.register(TestimonialsIntro,TestimonialsIntroAdmin)


