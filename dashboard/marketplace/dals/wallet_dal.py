import dataclasses
from typing import Optional, Tuple

from crypto.tron import TronMultiWallet, tron_multi_wallet
from dashboard.marketplace.app_models import Wallet, SupportedWalletCurrency, SupportedWalletSubnetworks, TelegramUser
from dashboard.marketplace.dals import BaseDAL
from dashboard.marketplace.dals.telegram_user_dal import TelegramUserDAL


@dataclasses.dataclass
class CreateWalletData:
    wallet_currency: Optional[str] = SupportedWalletCurrency.usdt
    wallet_subnetwork: Optional[str] = SupportedWalletSubnetworks.trc_20


class WalletDAL:

    def __init__(self):
        self.telegram_user_dal = TelegramUserDAL()

    @staticmethod
    async def generate_wallet(user: TelegramUser, wallet_data: CreateWalletData) -> Tuple[Optional[Wallet], bool]:
        wallet_id = user.id
        tron_wallet = await tron_multi_wallet.generate_address_by_id(wallet_id)
        if not tron_wallet.address or not tron_wallet.private_key:
            return None, False

        new_wallet, _ = Wallet.objects.get_or_create(
            user=user,
            wallet_address=tron_wallet.address,
            wallet_private_key=tron_wallet.private_key,

            defaults={
                'wallet_currency': wallet_data.wallet_currency,
                'wallet_subnetwork': wallet_data.wallet_subnetwork
            }
        )
        return new_wallet, _

    @BaseDAL.dal_logging_decorator
    async def create_wallet_by_user_id_if_not_exist(
            self, user_id: int,
            wallet_data: CreateWalletData = CreateWalletData()
    ) -> Tuple[Optional[Wallet], bool]:

        user = await self.telegram_user_dal.get_user_by_id(user_id)
        if user is None:
            return None, False

        return await self.generate_wallet(user, wallet_data)

    @BaseDAL.dal_logging_decorator
    async def create_wallet_by_user_if_not_exist(
            self, user: TelegramUser,
            wallet_data: CreateWalletData = CreateWalletData()
    ) -> Tuple[Optional[Wallet], bool]:

        return await self.generate_wallet(user, wallet_data)
