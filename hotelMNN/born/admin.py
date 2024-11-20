from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_type', 'price_per_night', 'available', 'date_added')
    list_filter = ('room_type', 'available')
    search_fields = ('title', 'detail')
