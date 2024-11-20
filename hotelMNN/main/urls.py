from django.urls import path
from .views import index, about, profile_view, register_view  # Убедитесь, что здесь есть register_view

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),  # Путь для регистрации
]
