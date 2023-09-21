from dataclasses import dataclass


class BaseConstants:
    @classmethod
    def get_choices(cls):
        return [
            (attr, getattr(cls, attr))
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        ]

    @classmethod
    def get_choice_max_length(cls):
        return max(max(len(str(choice[0])), len(str(choice[1]))) for choice in cls.get_choices())

    @classmethod
    def get_fields(cls) -> list:
        return [attr for attr, value in cls.__annotations__.items()]


@dataclass
class UserRole(BaseConstants):
    admin: str = 'admin'
    user: str = 'user'


@dataclass
class SupportedWalletCurrency(BaseConstants):
    usdt: str = 'USDT'
    tron: str = 'Tron'


@dataclass
class SupportedWalletSubnetworks(BaseConstants):
    trc_20: str = 'TRC-20'


@dataclass
class StatusState(BaseConstants):
    confirmed: str = 'Confirmed'
    canceled: str = 'Canceled'
    on_moderation: str = 'Moderation'


class ConstantsTelegramUser(BaseConstants):
    user_id: str = 'User ID'
    username: str = '@username'
    role: str = 'Role'
    balance: str = 'USDT Balance'
    rating: str = 'Rating'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ConstantsWallet(BaseConstants):
    wallet_id: str = 'Wallet ID'
    user: str = 'User'
    wallet_address: str = 'Wallet address'
    wallet_currency: str = 'Wallet currency'
    wallet_subnetwork: str = 'Wallet subnetwork'

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'


class ConstantsFile(BaseConstants):
    file_id: str = 'File ID'
    owner_user: str = 'Owner'
    file_name: str = 'File name'
    file_description: str = 'Description'
    file_dir: str = 'File path'
    file_price: str = 'Price'
    file_pub_date: str = 'Date published'
    file_status: str = 'Status'

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class ConstantsReview(BaseConstants):
    review_id = 'Review ID'
    review_message = 'Message'
    review_rate = 'Rate'
    review_date = 'Review date'
    owner_user = 'User'
    file = 'File'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
