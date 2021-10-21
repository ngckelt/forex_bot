from django.contrib import admin
from . import models


@admin.register(models.Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'account']

    class Meta:
        model = models.Clients


@admin.register(models.BotAdmins)
class BotAdminsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'active']

    class Meta:
        model = models.BotAdmins
