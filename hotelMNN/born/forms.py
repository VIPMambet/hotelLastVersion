from django import forms
from .models import Booking, AdditionalService

class BookingForm(forms.ModelForm):
    check_in = forms.DateField(
        label="Дата заезда",
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'дд.мм.гггг'})
    )
    check_out = forms.DateField(
        label="Дата выезда",
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'дд.мм.гггг'})
    )
    guests = forms.IntegerField(
        label="Количество гостей",
        initial=1,
    )
    guest_name = forms.CharField(
        label="Имя гостя",
        max_length=255,
        initial="Default Name",
    )
    guest_email = forms.EmailField(
        label="Электронная почта гостя",
        max_length=255,
        initial="default@example.com",
    )
    additional_services = forms.ModelMultipleChoiceField(
        queryset=AdditionalService.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Используем правильный виджет для чекбоксов
        required=False,
        label="Дополнительные услуги"
    )

    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'guests', 'guest_name', 'guest_email', 'additional_services']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавление класса для всех полей для улучшения стилей
        self.fields['check_in'].widget.attrs.update({'class': 'form-control'})
        self.fields['check_out'].widget.attrs.update({'class': 'form-control'})
        self.fields['guests'].widget.attrs.update({'class': 'form-control'})
        self.fields['guest_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['guest_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['additional_services'].widget.attrs.update({'class': 'form-check-input'})
