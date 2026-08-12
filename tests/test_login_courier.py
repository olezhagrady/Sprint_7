import allure


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier(self, api, courier):
        response = api.login_courier(
            courier["login"],
            courier["password"]
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация с неправильным логином")
    def test_login_wrong_login(self, api, courier):
        response = api.login_courier(
            "wrong_login",
            courier["password"]
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация с неправильным паролем")
    def test_login_wrong_password(self, api, courier):
        response = api.login_courier(
            courier["login"],
            "wrong_password"
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация без логина")
    def test_login_without_login(self, api, courier):
        response = api.login_courier(
            password=courier["password"]
        )

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для входа"
        )

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_nonexistent_user(self, api):
        response = api.login_courier(
            "nonexistent_login_123",
            "nonexistent_password_123"
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"