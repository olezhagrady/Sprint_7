import allure

from api import create_order
from data import (
    ORDER_DATA,
    ORDER_DATA_BLACK,
    ORDER_DATA_GREY,
    ORDER_DATA_BLACK_GREY
)


class TestCreateOrder:

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        response = create_order(ORDER_DATA)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с чёрным цветом")
    def test_create_order_with_black_color(self):
        response = create_order(ORDER_DATA_BLACK)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с серым цветом")
    def test_create_order_with_grey_color(self):
        response = create_order(ORDER_DATA_GREY)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с чёрным и серым цветами")
    def test_create_order_with_black_and_grey_colors(self):
        response = create_order(ORDER_DATA_BLACK_GREY)

        assert response.status_code == 201
        assert "track" in response.json()