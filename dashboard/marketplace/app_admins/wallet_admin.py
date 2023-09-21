from django.contrib import admin

from .base_admin import AutoConfigAdmin
from ..app_forms.wallet_form import WalletForm
from ..app_models import Wallet


@admin.register(Wallet)
class TelegramUserAdmin(AutoConfigAdmin):
    form = WalletForm
