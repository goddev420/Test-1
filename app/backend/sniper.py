from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solders.pubkey import Pubkey
import logging

class Sniper:
    def __init__(self, private_key, rpc_url):
        self.client = Client(rpc_url)
        self.private_key = private_key
        logging.basicConfig(level=logging.INFO)

    def buy_token(self, contract_address, amount):
        try:
            transaction = Transaction().add(
                transfer(TransferParams(
                    from_pubkey=Pubkey.from_string(self.private_key),
                    to_pubkey=Pubkey.from_string(contract_address),
                    lamports=amount
                ))
            )
            signature = self.client.send_transaction(transaction)
            logging.info(f"Transaction sent with signature: {signature}")
        except Exception as e:
            logging.error(f"Transaction failed: {e}")