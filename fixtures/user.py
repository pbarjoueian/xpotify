# content of conftest.py

import pytest


@pytest.fixture()
def normal_user(
    db: None,
    django_user_model,
):
    """A Django  user.

    This uses an existing user with email "user@test.com", or creates a new one with
    password "password".
    """
    UserModel = django_user_model
    email = "user@test.com"

    try:
        user = UserModel._default_manager.get_by_natural_key(email)
    except UserModel.DoesNotExist:
        user_data = {
            "email": email,
            "password": "password",
        }

        user = UserModel._default_manager.create_user(**user_data)
    return user
