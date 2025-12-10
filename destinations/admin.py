from django.contrib import admin
from .models import Destination, DestinationImage

class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1

class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationImageInline]
    list_display = ('place_name', 'state', 'district', 'weather')
    search_fields = ('place_name', 'state', 'district')
    list_filter = ('state', 'weather')

admin.site.register(Destination, DestinationAdmin)