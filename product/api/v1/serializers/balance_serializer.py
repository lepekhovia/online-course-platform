from rest_framework import serializers
from courses.models import Balance
from .user_serializer import CustomUserSerializer


class BalanceSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=6, decimal_places=0)
    user = CustomUserSerializer()

    class Meta:
        model = Balance
        fields = ['user', 'amount', 'id']
        read_only_fields = ['user']
