from django.contrib import admin

from ..forms import TelegramUserForm
from ..models import TelegramUser
from .base_admin import AutoConfigAdmin


@admin.register(TelegramUser)
class TelegramUserAdmin(AutoConfigAdmin):
    form = TelegramUserForm
