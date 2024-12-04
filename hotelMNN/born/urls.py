from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # Импортируем LogoutView

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),  # Путь для профиля
    # Главная страница бронирования
    path('booking/<int:room_id>/', views.booking_create, name='booking_create'),

    path('', views.bron_home, name='born_home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# Добавьте поддержку медиафайлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавьте поддержку статических файлов в режиме разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
