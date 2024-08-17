from django.db import models


class Balance(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, verbose_name='Пользователь', related_name='balance')
    amount = models.DecimalField(max_digits=6, decimal_places=0, default=1000)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.user.username} has {self.amount} in balance"
