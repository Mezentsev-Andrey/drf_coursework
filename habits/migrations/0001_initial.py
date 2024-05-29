# Generated by Django 4.2.9 on 2024-05-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=150, verbose_name="Место")),
                ("time", models.TimeField(verbose_name="Время когда выполнять")),
                ("action", models.CharField(max_length=150, verbose_name="Действие")),
                (
                    "sign_of_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.SmallIntegerField(default=1, verbose_name="Периодичность"),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(
                        blank=True, null=True, verbose_name="Время на выполнение"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "next_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата следующего действия"
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("id",),
            },
        ),
    ]
