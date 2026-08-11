import allure

from api import accept_order


class TestAcceptOrder:

    @allure.title("Успешное принятие заказа курьером")
    def test_accept_order(self, courier, order):
        response = accept_order(
            order["id"],
            courier["id"]
        )

        assert response.status_code == 200
        assert response.json()["ok"] is True

    @allure.title("Принятие заказа без идентификатора курьера")
    def test_accept_order_without_courier_id(self, order):
        response = accept_order(order["id"])

        assert response.status_code == 400
        assert "message" in response.json()