import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

#  Tron Multi Wallet
DEFAULT_MNEMONIC = 'exchange like head remind script runway teach gold arctic tree bird tiger'
DEFAULT_PASSPHRASE = None

MNEMONIC_PHRASE = os.getenv('MNEMONIC_PHRASE', default=DEFAULT_MNEMONIC)
PASSPHRASE = os.getenv('PASSPHRASE', default=DEFAULT_PASSPHRASE)
# ---

BASE_DIR = Path(__file__).parent.parent

#  Localization
LOCALES_DIR = BASE_DIR / 'locales'
I18N_DOMAIN = 'messages'

AVAILABLE_LANGUAGES = [lang for lang in os.listdir(LOCALES_DIR) if os.path.isdir(os.path.join(LOCALES_DIR, lang))]
DEFAULT_LANG = 'ua'
# ---

SUPPORT_SERVICE = 'san4o_prog'
