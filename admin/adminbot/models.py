from django.core.validators import MinValueValidator
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

    def __str__(self):
        return self.telegram_id

    class Meta:
        abstract = True


class Clients(Users):
    referer = models.CharField(verbose_name="Приведен пользователем", max_length=30, blank=True)
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    middle_name = models.CharField(verbose_name="Отчество", max_length=255)
    card_number = models.CharField(verbose_name="Номер карты", max_length=16)
    deposit = models.FloatField(verbose_name="Баланс", default=0, validators=[MinValueValidator(0.0)])
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



