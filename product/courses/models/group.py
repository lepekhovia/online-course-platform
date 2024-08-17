from django.db import models


def _set_number():
    return Group.objects.all().count() + 1


class Group(models.Model):
    number = models.CharField(
        max_length=10,
        verbose_name='Номер группы',
        default=_set_number
    )
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name='Курс',
        related_name='groups'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)
