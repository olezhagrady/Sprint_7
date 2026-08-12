import allure
import requests

from data import BASE_URL


class ScooterApi:

    @allure.step("Создание курьера")
    def create_courier(self, payload):
        return requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=payload,
            timeout=10
        )

    @allure.step("Авторизация курьера")
    def login_courier(self, login=None, password=None):
        payload = {}

        if login is not None:
            payload["login"] = login

        if password is not None:
            payload["password"] = password

        return requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json=payload,
            timeout=10
        )

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        return requests.delete(
            f"{BASE_URL}/api/v1/courier/{courier_id}",
            timeout=10
        )

    @allure.step("Создание заказа")
    def create_order(self, payload):
        return requests.post(
            f"{BASE_URL}/api/v1/orders",
            json=payload,
            timeout=10
        )

    @allure.step("Получение списка заказов")
    def get_orders(self):
        return requests.get(
            f"{BASE_URL}/api/v1/orders",
            timeout=30
        )

    @allure.step("Получение заказа по трек-номеру")
    def get_order_by_track(self, track):
        return requests.get(
            f"{BASE_URL}/api/v1/orders/track",
            params={"t": track},
            timeout=10
        )

    @allure.step("Принятие заказа")
    def accept_order(self, order_id, courier_id=None):
        params = None

        if courier_id is not None:
            params = {"courierId": courier_id}

        return requests.put(
            f"{BASE_URL}/api/v1/orders/accept/{order_id}",
            params=params,
            timeout=10
        )