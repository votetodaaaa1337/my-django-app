from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('service', 'client', 'worker', 'status', 'created_at')
    list_filter = ('status', 'worker')
    search_fields = ('client__username', 'worker__username', 'service__title')

admin.site.register(ConstructionRequest)