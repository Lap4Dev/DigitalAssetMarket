from django.core.validators import MinValueValidator
from django.db import models

from . import TelegramUser
from ._constants import ConstantsWithdraw, StatusState


class Withdraw(models.Model):
    id = models.AutoField(verbose_name=ConstantsWithdraw.id, primary_key=True)
    user = models.ForeignKey(TelegramUser, verbose_name=ConstantsWithdraw.user, on_delete=models.CASCADE)
    wallet = models.CharField(verbose_name=ConstantsWithdraw.wallet, max_length=256)
    amount = models.DecimalField(
        verbose_name=ConstantsWithdraw.amount,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    commission = models.DecimalField(
        verbose_name=ConstantsWithdraw.commission,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    status = models.CharField(
        verbose_name=ConstantsWithdraw.status,
        choices=StatusState.get_choices(),
        max_length=StatusState.get_choice_max_length(),
        default=StatusState.in_process
    )
    created_at = models.DateTimeField(verbose_name=ConstantsWithdraw.created_at, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=ConstantsWithdraw.updated_at, auto_now=True)

    def __str__(self):
        return f'Withdraw #{self.id} from {self.user}'

    class Meta(ConstantsWithdraw.Meta):
        ...
