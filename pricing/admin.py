from django.contrib import admin
from .models import PlanFeature, PricePlan
# Register your models here.

class PricePlanAdmin(admin.ModelAdmin):
    # filter_horizontal = ('plan_features',)
    pass


admin.site.register(PlanFeature)
admin.site.register(PricePlan,PricePlanAdmin)