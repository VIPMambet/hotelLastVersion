from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  # Импортируем ваши представления

urlpatterns = [
    path('accounts/profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_view, name='login'),  # Ваш кастомный вход
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_view, name='register'),
    path('feedback/', views.feedback_view, name='feedback'),

]
