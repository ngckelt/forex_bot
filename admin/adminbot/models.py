from django.db import models
from django.utils.timezone import now


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        abstract = True


class Users(TimeBasedModel):
    telegram_id = models.CharField(verbose_name="ID в телеграмме", max_length=255)
    username = models.CharField(verbose_name="Юзернейм в телеграмме", max_length=255, blank=True)

    class Meta:
        abstract = True


class Clients(Users):
    deposit = models.PositiveBigIntegerField(verbose_name="Счет", default=0)
    last_update_deposit_date = models.DateField(verbose_name="Последняя дата пополнения депозита", default=now)

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"


class Referrals(Users):
    referrer = models.ForeignKey(Clients, verbose_name="Реферер", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"


class BotAdmins(Users):
    active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Админ бота"
        verbose_name_plural = "Админы бота"



