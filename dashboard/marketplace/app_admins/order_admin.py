from django.contrib import admin
from .base_admin import AutoConfigAdmin
from ..app_forms.order_form import OrderForm
from ..app_models.order import Order


@admin.register(Order)
class OrderAdmin(AutoConfigAdmin):
    form = OrderForm
