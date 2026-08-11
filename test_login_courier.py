import allure

from api import login_courier


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier(self, courier):
        response = login_courier(
            courier["login"],
            courier["password"]
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация с неправильным логином")
    def test_login_wrong_login(self, courier):
        response = login_courier(
            "wrong_login",
            courier["password"]
        )

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Авторизация с неправильным паролем")
    def test_login_wrong_password(self, courier):
        response = login_courier(
            courier["login"],
            "wrong_password"
        )

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_without_login(self, courier):
        response = login_courier(
            password=courier["password"]
        )

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Авторизация с пустым паролем")
    def test_login_with_empty_password(self, courier):
        response = login_courier(
            login=courier["login"],
            password=""
        )

        assert response.status_code == 400
        assert "message" in response.json()