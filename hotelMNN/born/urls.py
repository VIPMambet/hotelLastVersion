from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница бронирования
    path('', views.bron_home, name='born_home'),


]

# Добавьте поддержку медиафайлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавьте поддержку статических файлов в режиме разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
