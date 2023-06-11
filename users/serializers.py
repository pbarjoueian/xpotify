from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "email", "history")
        read_only_fields = ("id", "first_name", "last_name", "email")
