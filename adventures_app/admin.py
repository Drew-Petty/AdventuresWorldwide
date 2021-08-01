from django.contrib import admin

# Register your models here.
from .models import Guide, Location, Category,Trip
admin.site.register(Trip)
admin.site.register(Guide)
admin.site.register(Location)
admin.site.register(Category)