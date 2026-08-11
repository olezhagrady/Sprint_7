import random
import string

from api import create_courier


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }


def register_new_courier_and_return_login_password():
    payload = generate_courier_payload()

    response = create_courier(payload)

    if response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать курьера: "
            f"{response.status_code}, {response.text}"
        )

    return payload