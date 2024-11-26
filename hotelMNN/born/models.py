from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Одноместный'),
        ('double', 'Двухместный'),
        ('suite', 'Люкс'),
    ]

    title = models.CharField('Название комнаты', max_length=50)
    detail = models.TextField('Описание', max_length=500)
    room_type = models.CharField('Тип комнаты', max_length=20, choices=ROOM_TYPES)
    price_per_night = models.DecimalField('Цена за ночь', max_digits=10, decimal_places=2)
    available = models.BooleanField('Доступна для бронирования', default=True)
    date_added = models.DateTimeField('Дата добавления', auto_now_add=True)
    image = models.ImageField('Фото комнаты', upload_to='img/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_room_type_display()})"

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Бронирование: {self.room} ({self.check_in} - {self.check_out})"
