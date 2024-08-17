from django.db import models


class Course(models.Model):
    """Модель продукта/курса."""
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="author_products"
    )
    name = models.CharField(
        max_length=264,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    started_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата начала",
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        verbose_name="Цена",
        null=True
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.name}, автор: {self.author.last_name} {self.author.first_name}"
