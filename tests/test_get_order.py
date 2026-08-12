import allure
from data import NONEXISTENT_TRACK


class TestGetOrderByTrack:

    @allure.title("Получение заказа по номеру")
    def test_get_order_by_track(self, api, order):
        response = api.get_order_by_track(order["track"])

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Получение заказа без номера")
    def test_get_order_without_track(self, api):
        response = api.get_order_by_track("")

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Получение заказа с несуществующим номером")
    def test_get_order_with_nonexistent_track(self, api):
        response = api.get_order_by_track("999999999999")

        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"

    @allure.title("Получение заказа с несуществующим номером")
    def test_get_order_with_nonexistent_track(self, api):
        response = api.get_order_by_track(NONEXISTENT_TRACK)

        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"