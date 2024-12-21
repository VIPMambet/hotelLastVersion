from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  # Импортируем ваши представления
from main.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView  # Добавляем импорт

urlpatterns = [
    path('accounts/profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_view, name='login'),  # Ваш кастомный вход
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_view, name='register'),
    path('feedback/', views.feedback_view, name='feedback'),

    # Добавим маршруты для сброса пароля
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
