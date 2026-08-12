import allure
import pytest

from data import (
    ORDER_DATA,
    ORDER_DATA_BLACK,
    ORDER_DATA_GREY,
    ORDER_DATA_BLACK_GREY
)


class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize(
        "order_data",
        [
            ORDER_DATA,
            ORDER_DATA_BLACK,
            ORDER_DATA_GREY,
            ORDER_DATA_BLACK_GREY
        ]
    )
    def test_create_order_with_different_colors(self, api, order_data):
        response = api.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()