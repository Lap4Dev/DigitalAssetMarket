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
    def get_fields(cls, exclude=None):
        if exclude is None:
            exclude = []

        field_names = list(cls.__annotations__.keys())

        return [field for field in field_names if field not in exclude]


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
    trc_20: str = 'TRC_20'


@dataclass
class StatusState(BaseConstants):
    confirmed: str = 'Confirmed'
    canceled: str = 'Canceled'
    in_process: str = 'In process'


class ConstantsTelegramUser(BaseConstants):
    id: str = 'ID'
    user_id: str = 'User ID'
    username: str = '@username'
    role: str = 'Role'
    balance: str = 'USDT Balance'
    rating: str = 'Rating'
    created_at: str = 'Created at'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ConstantsWallet(BaseConstants):
    wallet_id: str = 'Wallet ID'
    user: str = 'User'
    wallet_address: str = 'Wallet address'
    wallet_private_key: str = 'Wallet private key'
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
    review_id: str = 'Review ID'
    review_message: str = 'Message'
    review_rate: str = 'Rate'
    review_date: str = 'Review date'
    owner_user: str = 'User'
    file: str = 'File'

    class Meta:
        verbose_name: str = 'Review'
        verbose_name_plural: str = 'Reviews'


class ConstantsTransaction(BaseConstants):
    transaction_id: str = 'Transaction ID'
    wallet: str = 'Wallet'
    transfer_amount: str = 'Transfer amount'
    transaction_message: str = 'Transaction message'
    transaction_hash: str = 'Transaction hash'
    transaction_status: str = 'Status'
    created_at: str = 'Created at'
    updated_at: str = 'Updated at'

    class Meta:
        verbose_name: str = 'Transaction'
        verbose_name_plural: str = 'Transactions'


class ConstantsOrder(BaseConstants):
    order_id: str = 'Order ID'
    transaction: str = 'Transaction'
    user: str = 'User'
    file: str = 'File'
    order_amount: str = 'Order total amount'
    order_date: str = 'Order date'
    order_status: str = 'Status'

    class Meta:
        verbose_name: str = 'Order'
        verbose_name_plural: str = 'Orders'
