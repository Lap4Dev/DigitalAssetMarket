from django.contrib import admin

from .base_admin import AutoConfigAdmin
from ..app_forms import TransactionForm
from ..app_models import Transaction


@admin.register(Transaction)
class TelegramUserAdmin(AutoConfigAdmin):
    form = TransactionForm
