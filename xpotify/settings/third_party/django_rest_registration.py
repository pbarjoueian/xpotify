# https://django-rest-registration.readthedocs.io/en/latest/quickstart.html

REST_REGISTRATION = {
    "REGISTER_VERIFICATION_URL": "https://frontend-host/verify-user/",
    "RESET_PASSWORD_VERIFICATION_URL": "https://frontend-host/reset-password/",
    "REGISTER_EMAIL_VERIFICATION_URL": "https://frontend-host/verify-email/",
    "VERIFICATION_FROM_EMAIL": "no-reply@example.com",
    "USER_PUBLIC_FIELDS": [
        "id",
        "email",
        "first_name",
        "last_name",
    ],
    "USER_EDITABLE_FIELDS": [
        "first_name",
        "last_name",
    ],
}
