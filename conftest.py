import pytest

from api import (
    create_courier,
    create_order,
    delete_courier,
    get_order_by_track,
    login_courier
)
from data import ORDER_DATA
from helpers import generate_courier_payload


@pytest.fixture
def courier():
    payload = generate_courier_payload()

    create_response = create_courier(payload)

    if create_response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать курьера: "
            f"{create_response.status_code}, {create_response.text}"
        )

    login_response = login_courier(
        payload["login"],
        payload["password"]
    )

    if login_response.status_code != 200:
        raise RuntimeError(
            f"Не удалось авторизовать курьера: "
            f"{login_response.status_code}, {login_response.text}"
        )

    courier_id = login_response.json()["id"]

    yield {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "id": courier_id
    }

    delete_courier(courier_id)


@pytest.fixture
def order():
    response = create_order(ORDER_DATA)

    if response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать заказ: "
            f"{response.status_code}, {response.text}"
        )

    track = response.json()["track"]

    order_response = get_order_by_track(track)

    if order_response.status_code != 200:
        raise RuntimeError(
            f"Не удалось получить созданный заказ: "
            f"{order_response.status_code}, {order_response.text}"
        )

    yield {
        "track": track,
        "id": order_response.json()["order"]["id"]
    }