import allure

from api import delete_courier
from data import NONEXISTENT_COURIER_ID


class TestDeleteCourier:

    @allure.title("Успешное удаление курьера")
    def test_delete_courier(self, courier):
        response = delete_courier(courier["id"])

        assert response.status_code == 200
        assert response.json()["ok"] is True

    @allure.title("Удаление курьера без идентификатора")
    def test_delete_courier_without_id(self):
        response = delete_courier("")

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Удаление курьера с несуществующим идентификатором")
    def test_delete_nonexistent_courier(self):
        response = delete_courier(NONEXISTENT_COURIER_ID)

        assert response.status_code == 404
        assert "message" in response.json()