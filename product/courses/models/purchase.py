from django.db import models


class Purchase(models.Model):
    """Модель покупки(подписки) курса(на курс)"""
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name='Курс',
        related_name='purchases'
    )
    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user_purchases'
    )
    purchased_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата покупки',
    )
    is_subscription = models.BooleanField(
        default=False,
        verbose_name='Подписка',
    )
    subscription_end = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата окончания подписки',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.user.username} оплатил {self.course.name}" + \
               (f" на {self.subscription_end}" if self.is_subscription else "")
