import allure


class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders(self, api):
        response = api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)