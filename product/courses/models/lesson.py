from django.db import models


class Lesson(models.Model):
    """Модель урока."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name='Курс',
        related_name='lessons',
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title
