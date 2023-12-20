from dataclasses import dataclass

from dashboard.marketplace.dals.telegram_user_dal import ShowUserSchema
from data.config import SUPPORT_SERVICE, WITHDRAW_FEE_AMOUNT


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

    YES = InlineButton('Yes', 'yes')
    NO = InlineButton('No', 'no')


class Messages:
    ACTION_NOT_FOUND_ERROR = 'Sorry, but there is no such action :('
    WELCOME_MESSAGE = 'Welcome to the world of FileCryptoMarketplace - the first marketplace where file exchange has ' \
                      'become simpler and more secure thanks to cryptocurrency! Here, we emphasize' \
                      ' that you can purchase files only through unique links.\n\n' \
                      'With FileCryptoMarketplace, you don\'t buy files as usual. ' \
                      'Instead, you\'ll have the opportunity to gain access to valuable information and resources by ' \
                      'following reliable links that ensure the security of your purchase. Our system guarantees ' \
                      'reliable cryptocurrency payments and ensures that files are only accessible to those who have ' \
                      'the corresponding link.\n\n' \
                      'Let FileCryptoMarketplace become your trusted partner in the world ' \
                      'of file exchange, where security and convenience take precedence!'

    POP_UP_BALANCE = 'Please enter the amount by which you want to top up the balance: '
    INVALID_AMOUNT = 'The amount must be a number and greater then 0'
    WITHDRAW_FEE = f'The withdrawal fee is {WITHDRAW_FEE_AMOUNT}%'
    PRE_WITHDRAW = lambda amount: f'💰 Available amount: <code>{amount}</code>\n' \
                                  f'🤏 ({Messages.WITHDRAW_FEE})\n\n' \
                                  '➡️ Please enter the amount you wish to withdraw:'
    ENTER_USDT_WALLET = '💠 Please enter valid <b>USDT TRC-20</b> wallet:'
    AMOUNT_MUST_BE_LOWER_THEN_BALANCE = 'The amount must be lower then balance!'
    VALID_WALLET_ADDRESS = lambda wallet: '✒️ Make sure this is your <b>USDT TRC-20</b> network wallet address:\n' \
                                          f'<code>{wallet}</code>'
    ERROR_OCCURRED = 'Oops, an error occurred, please try again :('
    WITHDRAW_REQUEST_SUBMITTED = 'Withdrawal request successfully submitted!\n' \
                                 'The application is usually processed within 24 hours'

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

    @staticmethod
    def withdraw_request_notification(
            request_id: int, user_id: int, username: str,
            withdraw_amount: float, withdraw_address: str, commission: float
    ):
        return f"<b>(--- WITHDRAW REQUEST #{request_id}--- )</b>\n\n" \
               f"🥷 <b>@{username}</b> <b>[{user_id}]</b>\n" \
               f"💰 Amount: <code>{withdraw_amount:.2f}</code>\n" \
               f"🎁 Commission: <code>{commission:.2f}</code>\n" \
               f"🪙 For withdrawal: <code>{(withdraw_amount-commission):.2f}</code>\n\n" \
               f"💠 Address: <code>{withdraw_address}</code>"
