import allure

from api import get_order_by_track
from data import NONEXISTENT_TRACK


class TestGetOrderByTrack:

    @allure.title("Получение заказа по номеру")
    def test_get_order_by_track(self, order):
        response = get_order_by_track(order["track"])

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Получение заказа без номера")
    def test_get_order_without_track(self):
        response = get_order_by_track("")

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Получение заказа с несуществующим номером")
    def test_get_order_with_nonexistent_track(self):
        response = get_order_by_track(NONEXISTENT_TRACK)

        assert response.status_code == 404
        assert "message" in response.json()