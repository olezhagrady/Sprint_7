import requests

from data import BASE_URL


def create_courier(payload):
    return requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=payload,
        timeout=10
    )


def login_courier(login=None, password=None):
    payload = {}

    if login is not None:
        payload["login"] = login

    if password is not None:
        payload["password"] = password

    return requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json=payload,
        timeout=10
    )


def delete_courier(courier_id):
    return requests.delete(
        f"{BASE_URL}/api/v1/courier/{courier_id}",
        timeout=10
    )


def create_order(payload):
    return requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=payload,
        timeout=10
    )


def get_orders():
    return requests.get(
        f"{BASE_URL}/api/v1/orders",
        timeout=30
    )


def get_order_by_track(track):
    return requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track},
        timeout=10
    )


def accept_order(order_id, courier_id=None):
    params = None

    if courier_id is not None:
        params = {"courierId": courier_id}

    return requests.put(
        f"{BASE_URL}/api/v1/orders/accept/{order_id}",
        params=params,
        timeout=10
    )