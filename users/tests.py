import contextlib

import pytest
from django.contrib.auth import get_user_model

user_email = "normal@user.com"
user_email_admin = "admin@user.com"
User = get_user_model()


@pytest.mark.django_db
class TestUsersManagers:
    def test_create_user(self):
        user = User.objects.create_user(email=user_email, password="foo")

        assert user.email == user_email
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

        with contextlib.suppress(AttributeError):
            assert user.username is None

        with pytest.raises(TypeError):
            User.objects.create_user()
        with pytest.raises(TypeError):
            User.objects.create_user(email="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        user = User.objects.create_superuser(email=user_email_admin, password="foo")

        assert user.email == user_email_admin
        assert user.is_active
        assert user.is_staff
        assert user.is_superuser

        with contextlib.suppress(AttributeError):
            assert user.username is None

        with pytest.raises(ValueError):
            User.objects.create_superuser(
                email=user_email, password="foo", is_superuser=False
            )


@pytest.mark.django_db
def test_get_user_shortcut():
    user = User.objects.create_user(email=user_email, password="foo")

    assert User.get_by_pk(user.pk)
    assert User.get_by_email(user.email)


@pytest.mark.django_db
def test_get_by_natural_key(normal_user):
    assert User.objects.get_by_natural_key(normal_user.email)
    assert User.objects.get_by_natural_key(normal_user.email.upper())
