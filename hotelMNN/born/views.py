from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Room
from .forms import BookingForm
from django.http import HttpResponse
from .models import AdditionalService


def profile_view(request):
    # Получаем все бронирования текущего пользователя
    bookings = Booking.objects.filter(user=request.user)

    # Передаем данные в шаблон
    return render(request, 'main/profile.html', {'bookings': bookings})

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

    # Создаём форму для бронирования
    form = BookingForm()

    # Передаем отфильтрованные комнаты и форму в шаблон
    context = {'rooms': rooms, 'form': form}
    return render(request, 'born/born_home.html', context)


def booking_create(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Проверка доступности
    if not room.availability_status:
        return HttpResponse("Эта комната уже забронирована", status=400)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Извлекаем данные из формы
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            guests = form.cleaned_data['guests']

            # Создаем объект бронирования
            booking = Booking(
                room=room,
                user=request.user,
                check_in=check_in,
                check_out=check_out,
                guests=guests
            )

            # Сохраняем бронирование
            booking.save()

            # После сохранения бронирования обновляем статус комнаты
            room.availability_status = False
            room.save()

            return redirect('profile')
        else:
            # Обработка ошибок формы, если она невалидна
            return render(request, 'born/booking.html', {'form': form, 'room': room})

    else:
        form = BookingForm()

    return render(request, 'born/booking.html', {'form': form, 'room': room})



