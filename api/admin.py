from django.contrib import admin
from api.models import Charts

class ChartsAdmin(admin.ModelAdmin):
    fieldsets = [
            ('None',                {'fields': ['name']}),
            ('Data',                {'fields': ['data']})
            ]

# Register your models here.
admin.site.register(Charts, ChartsAdmin)
