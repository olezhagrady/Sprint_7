BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_DATA = {
    "password": "Password123",
    "firstName": "TestCourier"
}

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uzumaki",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-08-15",
    "comment": "Saske, come back to Konoha"
}

ORDER_DATA_BLACK = {
    **ORDER_DATA,
    "color": ["BLACK"]
}

ORDER_DATA_GREY = {
    **ORDER_DATA,
    "color": ["GREY"]
}

ORDER_DATA_BLACK_GREY = {
    **ORDER_DATA,
    "color": ["BLACK", "GREY"]
}

NONEXISTENT_COURIER_ID = 999999999
NONEXISTENT_TRACK = 999999999