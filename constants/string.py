from dataclasses import dataclass

from dashboard.marketplace.dals.telegram_user_dal import ShowUserSchema
from data.config import SUPPORT_SERVICE


class BotCommand:
    START = 'start'
    HELP = 'help'


class Helper:
    COMMAND_START_HELPER = 'Start interacting with bot'
    COMMAND_HELP_HELPER = 'Get bot help'


class Rating:
    POINT_1 = '1️⃣: 😞'
    POINT_2 = '2️⃣: 😕'
    POINT_3 = '3️⃣: 😐'
    POINT_4 = '4️⃣: 😊'
    POINT_5 = '5️⃣: 😍'


@dataclass
class InlineButton:
    name: str
    callback_data: str

    def __str__(self):
        return self.name


class Buttons:
    MAIN_MENU = InlineButton('Main menu', 'main_menu')
    PROFILE = InlineButton('Profile', 'profile')
    HELP = InlineButton('Care service', 'care_service')

    MY_PRODUCTS = InlineButton('My products', 'my_products')
    UPLOAD_FILE = InlineButton('Upload file', 'upload_file')

    BALANCE = InlineButton('Balance', 'balance')
    WITHDRAWAL_BALANCE = InlineButton('Withdrawal', 'withdrawal')
    TOP_UP_BALANCE = InlineButton('Top up', 'top_up')

    HISTORY = InlineButton('History', 'history')
    PURCHASE_HISTORY = InlineButton('Purchase history', 'purchase_history')
    SALES_HISTORY = InlineButton('Sales history', 'sales_history')

    GO_BACK = InlineButton('Return', 'return')
    CANCEL = InlineButton('Cancel', 'cancel')

    RATING = InlineButton('Rating', 'rating')


class Messages:
    ACTION_NOT_FOUND_ERROR = 'Sorry, but there is no such action :('
    WELCOME_MESSAGE = 'Welcome to the world of FileCryptoMarketplace - the first marketplace where file exchange has ' \
                      'become simpler and more secure thanks to cryptocurrency! Here, we emphasize that you can purchase' \
                      ' files only through unique links.\n\n' \
                      'With FileCryptoMarketplace, you don\'t buy files as usual. ' \
                      'Instead, you\'ll have the opportunity to gain access to valuable information and resources by ' \
                      'following reliable links that ensure the security of your purchase. Our system guarantees ' \
                      'reliable cryptocurrency payments and ensures that files are only accessible to those who have ' \
                      'the corresponding link.\n\n' \
                      'Let FileCryptoMarketplace become your trusted partner in the world ' \
                      'of file exchange, where security and convenience take precedence!'

    @staticmethod
    def get_profile_message(profile_info: ShowUserSchema):

        return f"🥷 <b>{profile_info.username}</b> <b>[{profile_info.user_id}]</b>\n\n" \
               f"💰 Balance: <code>{profile_info.balance}</code>\n\n" \
               f"📉 Number of Purchased Files: <code>{profile_info.purchased_files_count}</code>\n\n" \
               f"📈 Number of Sold Files: <code>{profile_info.sold_files_count}</code>\n\n" \
               f"⭐ Your Rating: <code>{profile_info.user_rating}</code>"

    CARE_SERVICE_MESSAGE = 'We are all imperfect! 😢\n\n' \
                           'If you have any difficulties with the functions or you have wishes to expand the' \
                           ' functionality, contact the care service manager @' + SUPPORT_SERVICE

    @staticmethod
    def get_balance_message(balance: float, username: str, user_id: int):

        return f"🥷 <b>{username}</b> <b>[{user_id}]</b>\n\n" \
               f"💰 Your balance: <code>{balance}</code>"
