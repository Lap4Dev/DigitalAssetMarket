from .base_forms import ChoicesModelForm
from ..app_models import Transaction, ConstantsTransaction


class TransactionForm(ChoicesModelForm):
    class Meta:
        model = Transaction
        fields = ConstantsTransaction.get_fields(exclude=['updated_at', 'created_at'])
