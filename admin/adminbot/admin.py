from django.contrib import admin
from . import models


@admin.register(models.Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'deposit']
    search_fields = ['telegram_id']

    class Meta:
        model = models.Clients


@admin.register(models.BotAdmins)
class BotAdminsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'active']
    search_fields = ['telegram_id']

    class Meta:
        model = models.BotAdmins


@admin.register(models.Referrals)
class ReferralsAdmin(admin.ModelAdmin):
    list_display = ['referrer']

    class Meta:
        model = models.Referrals
