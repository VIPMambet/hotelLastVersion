document.addEventListener("DOMContentLoaded", function() {
    // Получаем все кнопки "Забронировать"
    const bookingButtons = document.querySelectorAll('.btn-book');
    const modal = document.getElementById("bookingModal");
    const closeModal = document.querySelector(".close");

    // Функция для открытия модального окна
    function openModal() {
        modal.style.display = "flex";  // Показываем модальное окно
    }

    // Добавляем обработчик события на каждую кнопку "Забронировать"
    bookingButtons.forEach(button => {
        button.addEventListener('click', openModal);
    });

    // Закрытие модального окна при клике на крестик
    closeModal.addEventListener('click', function() {
        modal.style.display = "none";  // Скрываем модальное окно
    });

    // Закрытие модального окна при клике за его пределами
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = "none";  // Скрываем модальное окно
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Инициализация Flatpickr для полей ввода дат
    flatpickr(".flatpickr", {
        dateFormat: "Y-m-d",  // Формат даты
        minDate: "today",     // Минимальная дата - сегодняшняя
    });

    // Получаем все кнопки "Забронировать"
    const bookingButtons = document.querySelectorAll('.btn-book');
    const modal = document.getElementById("bookingModal");
    const closeModal = document.querySelector(".close");

    // Функция для открытия модального окна
    function openModal() {
        modal.style.display = "flex";  // Показываем модальное окно
    }

    // Добавляем обработчик события на каждую кнопку "Забронировать"
    bookingButtons.forEach(button => {
        button.addEventListener('click', openModal);
    });

    // Закрытие модального окна при клике на крестик
    closeModal.addEventListener('click', function() {
        modal.style.display = "none";  // Скрываем модальное окно
    });

    // Закрытие модального окна при клике за его пределами
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = "none";  // Скрываем модальное окно
        }
    });

    // Обработка отправки формы бронирования
    const bookingForm = document.getElementById('bookingForm');
    bookingForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Останавливаем отправку формы

        // Получаем значения из формы
        const checkinDate = document.getElementById('checkin-date').value;
        const checkoutDate = document.getElementById('checkout-date').value;
        const guests = document.getElementById('guests').value;

        // Выводим информацию в консоль (вы можете заменить это на реальную обработку)
        console.log(`Дата заезда: ${checkinDate}`);
        console.log(`Дата выезда: ${checkoutDate}`);
        console.log(`Количество гостей: ${guests}`);

        // Закрываем модальное окно
        modal.style.display = "none";

        // Можете добавить сюда логику отправки данных на сервер или отображения подтверждения.
    });
});


// Получение элементов для второго модального окна
const paymentModal = document.getElementById("paymentModal");
const closePaymentModal = document.getElementById("closePaymentModal");
const paymentForm = document.getElementById("paymentForm");

// Открытие второго модального окна при успешном подтверждении бронирования
document.getElementById("bookingForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Отключаем отправку формы
    document.getElementById("bookingModal").style.display = "none"; // Закрываем первое окно
    paymentModal.style.display = "block"; // Открываем окно оплаты
});

// Закрытие второго модального окна
closePaymentModal.onclick = function () {
    paymentModal.style.display = "none";
};

// Закрытие при клике вне окна
window.onclick = function (event) {
    if (event.target === paymentModal) {
        paymentModal.style.display = "none";
    }
};

// Обработка отправки формы оплаты
paymentForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Отключаем отправку формы для теста
    alert("Оплата успешно завершена!");
    paymentModal.style.display = "none"; // Закрываем окно после завершения
});


document.getElementById('payment-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const room = localStorage.getItem('selectedRoom');
    const checkIn = localStorage.getItem('checkInDate');
    const checkOut = localStorage.getItem('checkOutDate');
    const guests = localStorage.getItem('guestCount');
    const totalPrice = calculateTotalPrice(); // Функция для подсчёта цены

    fetch('/confirm-booking/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Убедись, что добавлен CSRF токен
        },
        body: JSON.stringify({
            room: room,
            check_in: checkIn,
            check_out: checkOut,
            guests: guests,
            total_price: totalPrice
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = '/profile/'; // Перенаправление в профиль
    });
});
