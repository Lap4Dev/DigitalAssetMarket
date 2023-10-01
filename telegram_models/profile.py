from dataclasses import dataclass


@dataclass
class TelegramProfile:
    chat_id: int = 0
    username: str = 'Unknown'
    balance: float = 0
    purchased_files_count: int = 0
    sold_files_count: int = 0
    user_rating: float = 0.0

