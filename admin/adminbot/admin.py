from django.contrib import admin
from . import models


@admin.register(models.Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'first_name', 'last_name', 'deposit', 'card_number', 'referer']
    search_fields = ['telegram_id', 'username', 'referer']

    class Meta:
        model = models.Clients


@admin.register(models.BotAdmins)
class BotAdminsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'active']
    search_fields = ['telegram_id']

    class Meta:
        model = models.BotAdmins


# @admin.register(models.Deposits)
# class DepositsAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'username', 'telegram_id', 'datetime', 'amount', 'card_number']
#     search_fields = ['first_name', 'last_name', 'username', 'telegram_id']
#
#     class Meta:
#         model = models.Deposits


# @admin.register(models.Withdrawals)
# class WithdrawalsAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'username', 'telegram_id', 'datetime', 'amount', 'card_number']
#     search_fields = ['first_name', 'last_name', 'username', 'telegram_id', 'datetime']
#
#     class Meta:
#         model = models.Withdrawals


# @admin.register(models.ReferralAccruals)
# class ReferralAccrualsAdmin(admin.ModelAdmin):
#     list_display = ['amount', 'accrual_to', 'accrual_from', 'datetime']
#     search_fields = ['accrual_to', 'accrual_from']
#
#     class Meta:
#         model = models.ReferralAccruals


# @admin.register(models.MonthlyAccruals)
# class MonthlyAccrualsAdmin(admin.ModelAdmin):
#     list_display = ['client', 'amount', 'datetime']
#     search_fields = ['client']
#
#     class Meta:
#         model = models.MonthlyAccruals


@admin.register(models.CardDetails)
class CardDetailsAdmins(admin.ModelAdmin):
    list_display = ['card_name', 'card_number']

    class Meta:
        model = models.CardDetails


@admin.register(models.BotTexts)
class BotTextsAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = models.BotTexts
