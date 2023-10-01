from .base_forms import ChoicesModelForm
from ..models import TelegramUser, ConstantsTelegramUser


class TelegramUserForm(ChoicesModelForm):
    class Meta:
        model = TelegramUser
        fields = ConstantsTelegramUser.get_fields(exclude=['created_at'])

