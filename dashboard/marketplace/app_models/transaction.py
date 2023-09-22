from django.core.validators import MinValueValidator
from django.db import models

from . import Wallet
from ._constants import ConstantsTransaction, StatusState


class Transaction(models.Model):
    transaction_id = models.AutoField(verbose_name=ConstantsTransaction.transaction_id, primary_key=True)
    wallet = models.ForeignKey(Wallet, verbose_name=ConstantsTransaction.wallet, on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(
        verbose_name=ConstantsTransaction.transfer_amount,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    transaction_hash = models.CharField(max_length=256, verbose_name=ConstantsTransaction.transaction_hash)
    transaction_status = models.CharField(
        verbose_name=ConstantsTransaction.transaction_status,
        choices=StatusState.get_choices(),
        max_length=StatusState.get_choice_max_length()
    )
    created_at = models.DateTimeField(verbose_name=ConstantsTransaction.created_at, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=ConstantsTransaction.updated_at, auto_now=True)

    def __str__(self):
        return f'Transaction #{self.transaction_id} from {self.wallet}'

    class Meta:
        verbose_name = ConstantsTransaction.Meta.verbose_name
        verbose_name_plural = ConstantsTransaction.Meta.verbose_name_plural
