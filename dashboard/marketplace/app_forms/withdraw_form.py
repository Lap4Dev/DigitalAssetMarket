from .base_forms import ChoicesModelForm
from ..app_models import Withdraw, ConstantsWithdraw


class WithdrawForm(ChoicesModelForm):
    class Meta:
        model = Withdraw
        fields = ConstantsWithdraw.get_fields(exclude=['created_at', 'updated_at'])
