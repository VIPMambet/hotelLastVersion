from django.contrib import admin
from .models import Room, Booking

# Настроим отображение бронирований в админке
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'guests', 'guest_name', 'guest_email')
    list_filter = ('check_in', 'check_out', 'room')  # Фильтры по дате и комнате
    search_fields = ('user__username', 'room__title', 'guest_name', 'guest_email')  # Поиск по пользователю и комнате

# Настроим отображение комнат в админке
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_type', 'price_per_night', 'availability_status', 'date_added')  # Убедитесь, что поле 'available' существует в модели
    list_filter = ('room_type', 'availability_status')  # Фильтры по типу комнаты и доступности
    search_fields = ('title', 'detail')  # Поиск по названию комнаты и деталям

from django.contrib import admin
from .models import AdditionalService

class AdditionalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

admin.site.register(AdditionalService, AdditionalServiceAdmin)
