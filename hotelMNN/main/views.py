from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm  # Импорт формы регистрации

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'main/profile.html', {'user': request.user})
