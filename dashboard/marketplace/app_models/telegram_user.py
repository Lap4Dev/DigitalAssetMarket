from django.db import models

from ._constants import ConstantsTelegramUser, UserRole


class TelegramUser(models.Model):
    user_id = models.IntegerField(verbose_name=ConstantsTelegramUser.user_id, primary_key=True)
    username = models.CharField(verbose_name=ConstantsTelegramUser.username, max_length=32, default=None)

    role = models.CharField(
        verbose_name=ConstantsTelegramUser.role,
        choices=UserRole.get_choices(),
        max_length=UserRole.get_choice_max_length()
    )

    balance = models.DecimalField(
        verbose_name=ConstantsTelegramUser.balance,
        decimal_places=2,
        max_digits=12,
        default=0
    )
    rating = models.DecimalField(verbose_name=ConstantsTelegramUser.rating, max_digits=3, decimal_places=2)

    def __str__(self):
        return f'User: {self.username}({self.user_id})'

    class Meta:
        verbose_name = ConstantsTelegramUser.Meta.verbose_name
        verbose_name_plural = ConstantsTelegramUser.Meta.verbose_name_plural
