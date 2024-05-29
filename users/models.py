from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="Город", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    chat_id = models.CharField(unique=True, max_length=50, verbose_name="Телеграм", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
