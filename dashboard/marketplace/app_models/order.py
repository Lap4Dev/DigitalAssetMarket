from django.core.validators import MinValueValidator
from django.db import models

from . import Transaction, TelegramUser, File
from ._constants import ConstantsOrder, StatusState


class Order(models.Model):
    order_id = models.AutoField(verbose_name=ConstantsOrder.order_id, primary_key=True)
    transaction = models.ForeignKey(Transaction, verbose_name=ConstantsOrder.transaction, on_delete=models.CASCADE)
    user = models.ForeignKey(TelegramUser, verbose_name=ConstantsOrder.user, on_delete=models.CASCADE)
    file = models.ForeignKey(File, verbose_name=ConstantsOrder.file, on_delete=models.CASCADE)
    order_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name=ConstantsOrder.order_amount
    )
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=ConstantsOrder.order_date)
    order_status = models.CharField(
        choices=StatusState.get_choices(),
        max_length=StatusState.get_choice_max_length(),
        verbose_name=ConstantsOrder.order_status
    )

    def __str__(self):
        return f'Order #{self.order_id} of {self.user}'

    class Meta:
        verbose_name = ConstantsOrder.Meta.verbose_name
        verbose_name_plural = ConstantsOrder.Meta.verbose_name_plural
