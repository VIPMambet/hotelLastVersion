from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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
    # Получаем все бронирования текущего пользователя
    bookings = Booking.objects.filter(user=request.user)

    # Если бронирований нет, передаем None в контекст
    if not bookings:
        bookings = None

    return render(request, 'main/profile.html', {'user': request.user, 'bookings': bookings})

# Страница с отзывами
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

# Представления для сброса пароля
class CustomPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset_form.html'  # Ваш шаблон для формы сброса пароля
    email_template_name = 'main/password_reset_email.html'  # Шаблон письма с ссылкой для сброса пароля
    subject_template_name = 'main/password_reset_subject.txt'  # Тема письма

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/password_reset_complete.html'
