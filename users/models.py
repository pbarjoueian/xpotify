from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with this email already exists."),
        },
    )
    history = models.JSONField(null=True, blank=True, default=list)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @classmethod
    def get_by_pk(cls, pk: int):
        """
        shortcut for getting user with pk
        :param pk:
        :return:
        """
        return cls.objects.get(pk=pk)

    @classmethod
    def get_by_email(cls, email: str):
        """
        shortcut for getting user with email address
        :param pk:
        :return:
        """
        return cls.objects.get(email=email)
