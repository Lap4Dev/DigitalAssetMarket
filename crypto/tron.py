import dataclasses
from typing import Optional

import base58
import requests
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import TronMainnet
from hdwallet.derivations import BIP44Derivation
from loguru import logger

from data.config import MNEMONIC_PHRASE, PASSPHRASE


@dataclasses.dataclass
class WalletSchema:
    address_index: Optional[int] = None
    address: Optional[str] = None
    private_key: Optional[str] = None


class TronMultiWallet:
    CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT
    API_URL_BASE = 'https://api.trongrid.io/'
    METHOD_BALANCE_OF = 'balanceOf(address)'

    def __init__(self, mnemonic=None, passphrase=None):
        self.mnemonic = mnemonic
        self.passphrase = passphrase

    @staticmethod
    def convert_address_to_parameter(addr):
        return "0" * 24 + base58.b58decode_check(addr)[1:].hex()

    async def init_tron_wallet(self) -> Optional[BIP44HDWallet]:
        try:
            bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=TronMainnet)
            bip44_hdwallet.from_mnemonic(
                mnemonic=self.mnemonic, language="english", passphrase=self.passphrase
            )
            bip44_hdwallet.clean_derivation()
            return bip44_hdwallet
        except Exception as ex:
            logger.error(ex)
            return None

    async def generate_address_by_id(self, address_index=0) -> WalletSchema:
        try:
            bip44_hdwallet = await self.init_tron_wallet()
            if bip44_hdwallet is None:
                return WalletSchema()

            bip44_derivation: BIP44Derivation = BIP44Derivation(
                cryptocurrency=TronMainnet, account=0, change=False, address=address_index
            )
            bip44_hdwallet.from_path(path=bip44_derivation)
            path = bip44_hdwallet.path()
            address = bip44_hdwallet.address()
            private_key = bip44_hdwallet.private_key()

            logger.info(f"({address_index}) {path} {address} 0x{private_key}")
            bip44_hdwallet.clean_derivation()

            return WalletSchema(address_index, address, private_key)

        except Exception as ex:
            logger.error(ex)
            return WalletSchema()

    async def get_balance_by_address(self, address='') -> int:
        try:
            url = self.API_URL_BASE + 'wallet/triggerconstantcontract'
            payload = {
                'owner_address': base58.b58decode_check(address).hex(),
                'contract_address': base58.b58decode_check(self.CONTRACT).hex(),
                'function_selector': self.METHOD_BALANCE_OF,
                'parameter': self.convert_address_to_parameter(address),
            }
            resp = requests.post(url, json=payload)
            data = resp.json()
            logger.info(data)

            if data['result'].get('result', None):
                val = data['constant_result'][0]
                return int(val, 16)
            else:
                logger.error(bytes.fromhex(data['result']['message']).decode())
                return 0
        except Exception as ex:
            logger.error(ex)
            return 0


tron_multi_wallet = TronMultiWallet(mnemonic=MNEMONIC_PHRASE, passphrase=PASSPHRASE)
