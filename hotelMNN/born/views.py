from django.shortcuts import render
from .models import Room

def bron_home(request):
    # Получаем все комнаты
    rooms = Room.objects.all()

    # Фильтрация по типу комнаты
    room_type = request.GET.get('room_type')
    if room_type:
        rooms = rooms.filter(room_type=room_type)

    # Фильтрация по диапазону цены
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        rooms = rooms.filter(price_per_night__gte=min_price)
    if max_price:
        rooms = rooms.filter(price_per_night__lte=max_price)

    # Передаем отфильтрованные комнаты в шаблон
    context = {'rooms': rooms}
    return render(request, 'born/born_home.html', context)
