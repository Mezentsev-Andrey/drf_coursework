from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Пользователь",
    )
    place = models.CharField(max_length=150, verbose_name="Место")
    time = models.TimeField(verbose_name="Время когда выполнять")
    action = models.CharField(max_length=150, verbose_name="Действие")
    sign_of_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "Habit",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        **NULLABLE,
    )
    periodicity = models.SmallIntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(max_length=150, verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.DurationField(
        verbose_name="Время на выполнение", **NULLABLE
    )
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    next_date = models.DateField(**NULLABLE, verbose_name="Дата следующего действия")

    def __str__(self):
        return f"{self.user} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)
