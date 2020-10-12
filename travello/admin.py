from django.contrib import admin

# Register your models here.
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Destination, DestinationAdmin)
