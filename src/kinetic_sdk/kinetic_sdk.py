# pylint: disable=missing-function-docstring,missing-class-docstring,too-many-arguments,fixme
"""Kinetic Sdk"""
from typing import Dict, List, Optional

from kinetic_sdk.generated.client.model.commitment import Commitment
from kinetic_sdk.helpers.validate_kinetic_sdk_config import validate_kinetic_sdk_config
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.kinetic_sdk_internal import KineticSdkInternal
from kinetic_sdk.models import PublicKeyString, TransactionType


class KineticSdk:
    def __init__(self, sdk_config):
        self.sdk_config = sdk_config
        self.internal = KineticSdkInternal(self.sdk_config)

    @property
    def config(self):
        return self.internal.app_config

    def close_account(
        self,
        account: PublicKeyString,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
        reference: Optional[str] = None,
    ):
        return self.internal.close_account(account, commitment, mint, reference)

    def create_account(
        self,
        owner: Keypair,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
        reference: Optional[str] = None,
    ):
        return self.internal.create_account(owner, commitment, mint, reference)

    def get_account_info(
        self,
        account: PublicKeyString,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
    ):
        return self.internal.get_account_info(account, commitment, mint)

    def get_balance(self, account: PublicKeyString):
        return self.internal.get_balance(account)

    def get_explorer_url(self, path: str):
        return self.internal.get_explorer_url(path)

    def get_history(self, account: PublicKeyString, mint: Optional[PublicKeyString] = None):
        return self.internal.get_history(account, mint)

    def get_kinetic_transaction(self, signature: Optional[str] = None, reference: Optional[str] = None):
        return self.internal.get_kinetic_transaction(signature, reference)

    def get_token_accounts(self, account: PublicKeyString, mint: Optional[PublicKeyString] = None):
        return self.internal.get_token_accounts(account, mint)

    def get_transaction(self, signature: str, commitment: Optional[Commitment] = None):
        return self.internal.get_transaction(signature, commitment)

    def make_transfer(
        self,
        owner: Keypair,
        destination: PublicKeyString,
        amount: str,
        tx_type: TransactionType = TransactionType.NONE,
        mint: Optional[PublicKeyString] = None,
        commitment: Optional[Commitment] = None,
        reference: Optional[str] = None,
        sender_create: bool = False,
    ):
        return self.internal.make_transfer(
            owner, destination, amount, mint, tx_type, reference, sender_create, commitment
        )

    def make_transfer_batch(
        self,
        owner: Keypair,
        destinations: List[Dict[PublicKeyString, str]],
        tx_type: TransactionType = TransactionType.NONE,
        mint: Optional[PublicKeyString] = None,
        commitment: Optional[Commitment] = None,
        reference: Optional[str] = None,
    ):
        return self.internal.make_transfer_batch(owner, destinations, mint, tx_type, reference, commitment)

    def request_airdrop(
        self,
        account: PublicKeyString,
        amount: str,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
    ):
        return self.internal.request_airdrop(
            account,
            amount,
            commitment,
            mint,
        )

    def init(self):
        # TODO: Add logging like in the other SDKs
        self.internal.get_app_config(self.sdk_config["environment"], self.sdk_config["index"])
        # TODO: Set up Solana instance

    @staticmethod
    def setup(endpoint, environment, index, headers=None):
        # TODO: Add logging like in the other SDKs
        sdk = KineticSdk(
            validate_kinetic_sdk_config(
                {"endpoint": endpoint, "environment": environment, "index": index, "headers": headers}
            )
        )
        sdk.init()
        return sdk
