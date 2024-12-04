from django.contrib import admin
from .models import Feedback

# Создаем класс для настройки отображения модели Feedback в админке
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback', 'created_at')  # Поля, которые будут отображаться в списке
    search_fields = ('name', 'feedback')  # Поля для поиска в админке
    list_filter = ('created_at',)  # Фильтрация по дате

# Регистрируем модель в админке
admin.site.register(Feedback, FeedbackAdmin)
