from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from courses.models import Purchase

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""
    amount = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'balance',
            'amount'
        ]

    def get_amount(self):
        return self.balance.first().amount


class PurchaseSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    # TODO

    class Meta:
        model = Purchase
        fields = (
            # TODO
        )
