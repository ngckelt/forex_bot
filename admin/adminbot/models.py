from django.db import models


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        abstract = True


class Users(TimeBasedModel):
    telegram_id = models.CharField(verbose_name="ID в телеграмме", max_length=255)

    class Meta:
        abstract = True


class Clients(Users):
    account = models.PositiveBigIntegerField(verbose_name="Счет", default=0)

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"


class BotAdmins(Users):
    active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Админ бота"
        verbose_name_plural = "Админы бота"



