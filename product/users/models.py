from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    STUDENT = "student"
    TEACHER = "teacher"
    STATUS_CHOICES = [
        (STUDENT, "Студент"),
        (TEACHER, "Преподаватель"),
    ]

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STUDENT,
        verbose_name='Статус'
    )
    group = models.ForeignKey(
        "courses.Group",
        verbose_name='Группы',
        related_name='students',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)
        unique_together = ()

    def __str__(self):
        return f" ({self.status})" + self.get_full_name()
