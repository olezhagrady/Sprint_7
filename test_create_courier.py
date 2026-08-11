import allure

from api import create_courier
from data import CREATE_COURIER_DATA
from helpers import generate_courier_payload


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier(self):
        payload = generate_courier_payload()

        response = create_courier(payload)

        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_with_existing_login(self, courier):
        payload = {
            **CREATE_COURIER_DATA,
            "login": courier["login"]
        }

        response = create_courier(payload)

        assert response.status_code == 409
        assert "message" in response.json()

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        payload = {
            "password": CREATE_COURIER_DATA["password"],
            "firstName": CREATE_COURIER_DATA["firstName"]
        }

        response = create_courier(payload)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        payload = {
            "login": generate_courier_payload()["login"],
            "firstName": CREATE_COURIER_DATA["firstName"]
        }

        response = create_courier(payload)

        assert response.status_code == 400
        assert "message" in response.json()