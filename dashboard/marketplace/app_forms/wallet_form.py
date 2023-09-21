from .base_forms import ChoicesModelForm
from ..app_models import Wallet, ConstantsWallet


class WalletForm(ChoicesModelForm):
    class Meta:
        model = Wallet
        fields = ConstantsWallet.get_fields()
