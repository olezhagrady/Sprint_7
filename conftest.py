import pytest
import time

from api import ScooterApi
from data import ORDER_DATA
from helpers import generate_courier_payload


@pytest.fixture
def api():
    return ScooterApi()


@pytest.fixture
def courier(api):
    payload = generate_courier_payload()

    create_response = api.create_courier(payload)

    if create_response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать курьера: "
            f"{create_response.status_code}, {create_response.text}"
        )

    login_response = api.login_courier(
        payload["login"],
        payload["password"]
    )

    if login_response.status_code != 200:
        raise RuntimeError(
            f"Не удалось авторизовать курьера: "
            f"{login_response.status_code}, {login_response.text}"
        )

    courier_id = login_response.json()["id"]

    try:
        yield {
            "login": payload["login"],
            "password": payload["password"],
            "firstName": payload["firstName"],
            "id": courier_id
        }
    finally:
        api.delete_courier(courier_id)


@pytest.fixture
def order(api):
    response = api.create_order(ORDER_DATA)

    if response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать заказ: "
            f"{response.status_code}, {response.text}"
        )

    track = response.json()["track"]

    for _ in range(5):
        order_response = api.get_order_by_track(track)

        if order_response.status_code == 200:
            yield {
                "track": track,
                "id": order_response.json()["order"]["id"]
            }
            return

        time.sleep(1)

    raise RuntimeError(
        f"Не удалось получить созданный заказ: "
        f"{order_response.status_code}, {order_response.text}"
    )