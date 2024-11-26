from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm  # Импорт формы регистрации
from django.contrib.auth.decorators import login_required
from born.models import Booking


# Главная страница
def index(request):
    return render(request, 'main/index.html')


# Страница о нас
def about(request):
    return render(request, 'main/about.html')


# Регистрация
def register_view(request):
    # Если пользователь уже авторизован, перенаправляем его на профиль
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})


# Вход
def login_view(request):
    # Если пользователь уже авторизован, перенаправляем его на главную страницу
    if request.user.is_authenticated:
        return redirect('home')  # Перенаправление на главную страницу

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после успешного входа
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})


# Профиль
@login_required
def profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'main/profile.html', {'user': request.user, 'bookings': bookings})



from django.shortcuts import render

def profile1_view(request):
    return render(request, 'main/profile.html')  # Шаблон, который вы хотите отобразить
