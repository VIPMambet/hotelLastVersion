from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm  # Импорт формы регистрации
# main/views.py
from born.models import Booking  # Импорт модели Booking из приложения born
from django.shortcuts import render
# main/views.py
from django.shortcuts import render, redirect
from .models import Feedback
from django.shortcuts import render


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


def feedback_view(request):
    feedbacks = ...  # Логика получения отзывов
    return render(request, 'main/feedback.html', {'feedbacks': feedbacks})


# Профиль
@login_required
def profile_view(request):
    # Получаем все бронирования текущего пользователя
    bookings = Booking.objects.filter(user=request.user)

    # Если бронирований нет, передаем None в контекст
    if not bookings:
        bookings = None

    return render(request, 'main/profile.html', {'user': request.user, 'bookings': bookings})

# Представление для страницы отзывов
# main/views.py
from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        feedback = request.POST.get('feedback')

        new_feedback = Feedback(name=name, feedback=feedback)
        new_feedback.save()

        return redirect('feedback')

    # Получаем все отзывы
    feedbacks = Feedback.objects.all()

    return render(request, 'main/feedback.html', {'feedbacks': feedbacks})

