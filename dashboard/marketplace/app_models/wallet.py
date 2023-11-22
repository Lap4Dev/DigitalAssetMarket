from django.db import models
from ._constants import ConstantsWallet, SupportedWalletCurrency, SupportedWalletSubnetworks
from .telegram_user import TelegramUser


class Wallet(models.Model):
    wallet_id = models.AutoField(verbose_name=ConstantsWallet.wallet_id, primary_key=True)
    user = models.ForeignKey(TelegramUser, verbose_name=ConstantsWallet.user, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=256, verbose_name=ConstantsWallet.wallet_address)
    wallet_private_key = models.CharField(
        max_length=256,
        verbose_name=ConstantsWallet.wallet_private_key,
        default=""
    )
    print(SupportedWalletSubnetworks.get_choices())
    wallet_currency = models.CharField(
        verbose_name=ConstantsWallet.wallet_currency,
        choices=SupportedWalletCurrency.get_choices(),
        max_length=SupportedWalletCurrency.get_choice_max_length()
    )
    wallet_subnetwork = models.CharField(
        verbose_name=ConstantsWallet.wallet_subnetwork,
        choices=SupportedWalletSubnetworks.get_choices(),
        max_length=SupportedWalletSubnetworks.get_choice_max_length()
    )

    def __str__(self):
        return f'Wallet #{self.wallet_id} of {self.user}'

    class Meta:
        verbose_name = ConstantsWallet.Meta.verbose_name
        verbose_name_plural = ConstantsWallet.Meta.verbose_name_plural
