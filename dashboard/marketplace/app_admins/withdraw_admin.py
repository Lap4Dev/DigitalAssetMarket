from django.contrib import admin

from .base_admin import AutoConfigAdmin
from ..app_forms import WithdrawForm
from ..app_models import Withdraw


@admin.register(Withdraw)
class WithdrawAdmin(AutoConfigAdmin):
    form = WithdrawForm
