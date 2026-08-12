import allure

from api import ScooterApi
from data import CREATE_COURIER_DATA
from helpers import generate_courier_payload


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier(self, api):
        payload = generate_courier_payload()

        try:
            response = api.create_courier(payload)

            assert response.status_code == 201
            assert response.json()["ok"] is True

        finally:
            login_response = api.login_courier(
                payload["login"],
                payload["password"]
            )

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                api.delete_courier(courier_id)

    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_with_existing_login(self, api, courier):
        payload = {
            **CREATE_COURIER_DATA,
            "login": courier["login"]
        }

        response = api.create_courier(payload)

        assert response.status_code == 409
        assert response.json()["message"] == (
            "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self, api):
        payload = {
            "password": CREATE_COURIER_DATA["password"],
            "firstName": CREATE_COURIER_DATA["firstName"]
        }

        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self, api):
        payload = generate_courier_payload()
        payload.pop("password")

        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )