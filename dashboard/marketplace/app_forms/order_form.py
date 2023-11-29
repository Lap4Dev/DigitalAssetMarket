from .base_forms import ChoicesModelForm
from ..app_models._constants import ConstantsOrder
from ..app_models.order import Order


class OrderForm(ChoicesModelForm):
    class Meta:
        model = Order
        fields = ConstantsOrder.get_fields(exclude='order_date')

