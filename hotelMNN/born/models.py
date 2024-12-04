from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Модель AdditionalService
class AdditionalService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

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
    availability_status = models.BooleanField('Доступна для бронирования', default=True)  # оставляем только это поле
    date_added = models.DateTimeField('Дата добавления', auto_now_add=True)
    image = models.ImageField('Фото комнаты', upload_to='img/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_room_type_display()})"

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


# Модель Booking
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    guest_name = models.CharField(max_length=255, default='Default Name')
    guest_email = models.EmailField(default='default@example.com')
    additional_services = models.ManyToManyField(AdditionalService, blank=True)



    def delete(self, *args, **kwargs):
        # Проверяем статус доступности комнаты перед удалением
        if not self.room.availability_status:  # если room забронирована, то availability_status будет False
            self.room.availability_status = True  # Сбрасываем статус доступности (делаем комнату доступной)
            self.room.save()  # Сохраняем изменения
        super().delete(*args, **kwargs)  # Выполняем удаление бронирования

    def __str__(self):
        return f'Бронирование {self.guest_name} в комнате {self.room.title}'


# Сигнал для обновления статуса комнаты при бронировании
@receiver(pre_save, sender=Booking)
def update_room_availability(sender, instance, **kwargs):
    if instance.room.availability_status is False:
        raise ValueError("Эта комната уже забронирована")
    else:
        # Если комната доступна, обновляем статус комнаты на забронированную
        instance.room.availability_status = False
        instance.room.save()  # Сохраняем изменения в статусе
