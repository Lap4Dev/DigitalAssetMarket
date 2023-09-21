import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

BASE_DIR = Path(__file__).parent.parent

LOCALES_DIR = BASE_DIR / 'locales'
I18N_DOMAIN = 'messages'

AVAILABLE_LANGUAGES = [lang for lang in os.listdir(LOCALES_DIR) if os.path.isdir(os.path.join(LOCALES_DIR, lang))]
DEFAULT_LANG = 'ua'
