from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from courses.models import Group, Purchase, Balance
from users.models import CustomUser


@receiver(post_save, sender=Purchase)
def post_save_subscription(sender, instance: Purchase, created, **kwargs):
    """
    Распределение нового студента в группу курса.
    """

    if created:
        pass


@receiver(post_save, sender=CustomUser)
def create_user_balance(sender, instance, created, **kwargs):
    """Начисление 1000 бонусов на счёт при создании пользователя."""
    if created:
        Balance.objects.create(user=instance, amount=1000)
