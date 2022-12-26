# pylint: disable=missing-function-docstring,missing-class-docstring,too-many-arguments,too-many-locals,fixme
"""Kinetic SDK Internal"""
from typing import Optional

import pybase64
from solana.publickey import PublicKey
from spl.token.instructions import get_associated_token_address

from kinetic_sdk.generated.client import ApiClient, Configuration
from kinetic_sdk.generated.client.api.account_api import AccountApi
from kinetic_sdk.generated.client.api.airdrop_api import AirdropApi
from kinetic_sdk.generated.client.api.app_api import AppApi
from kinetic_sdk.generated.client.api.transaction_api import TransactionApi
from kinetic_sdk.generated.client.model.app_config_mint import AppConfigMint
from kinetic_sdk.generated.client.model.close_account_request import CloseAccountRequest
from kinetic_sdk.generated.client.model.commitment import Commitment
from kinetic_sdk.generated.client.model.create_account_request import CreateAccountRequest
from kinetic_sdk.generated.client.model.make_transfer_request import MakeTransferRequest
from kinetic_sdk.generated.client.model.request_airdrop_request import RequestAirdropRequest
from kinetic_sdk.helpers.generate_create_account_transaction import generate_create_account_transaction
from kinetic_sdk.helpers.generate_make_transfer_batch_transaction import generate_make_transfer_batch_transaction
from kinetic_sdk.helpers.generate_make_transfer_transaction import generate_make_transfer_transaction
from kinetic_sdk.helpers.get_public_key import get_public_key
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models.public_key_string import PublicKeyString
from kinetic_sdk.models.transaction_type import TransactionType
from kinetic_sdk.models.version import NAME, VERSION


class KineticSdkInternal:
    def __init__(self, config):
        self.app_config = None
        self.sdk_config = config

        # Create the API configuration
        configuration = Configuration(host=self.sdk_config["endpoint"], discard_unknown_keys=True)
        api_client = self._api_base_options(configuration, config)

        # Create the API instances
        self.account_api = AccountApi(api_client)
        self.airdrop_api = AirdropApi(api_client)
        self.app_api = AppApi(api_client)
        self.transaction_api = TransactionApi(api_client)

    def close_account(
        self,
        account: PublicKeyString,
        commitment: Commitment,
        mint: PublicKeyString,
        reference_id: str,
        reference_type: str,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        request = CloseAccountRequest(
            account=get_public_key(account),
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            mint=mint.public_key,
            reference_id=reference_id,
            reference_type=reference_type,
        )

        return self.account_api.close_account(request)

    def create_account(
        self,
        owner: Keypair,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
        reference_id: Optional[str] = None,
        reference_type: Optional[str] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        blockhash = self._get_block_hash_height(self.sdk_config["environment"], self.sdk_config["index"])

        tx = generate_create_account_transaction(
            add_memo=mint.add_memo,
            blockhash=blockhash["blockhash"],
            index=self.sdk_config["index"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=mint.public_key,
            owner=owner,
        )

        request = CreateAccountRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=mint.public_key,
            reference_id=reference_id,
            reference_type=reference_type,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.account_api.create_account(request)

    def get_account_info(
        self,
        account: PublicKeyString,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        return self.account_api.get_account_info(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            mint.public_key,
            commitment,
        )

    def get_app_config(self, environment, index):
        self.app_config = self.app_api.get_app_config(environment, index)

        return self.app_config

    def get_balance(self, account: PublicKeyString, commitment: Optional[Commitment] = None):
        commitment = self._get_commitment(commitment)

        return self.account_api.get_balance(
            self.sdk_config["environment"], self.sdk_config["index"], get_public_key(account), commitment
        )

    def get_explorer_url(self, path: str):
        return self.app_config["environment"]["explorer"].replace("{path}", path)

    def get_history(
        self,
        account: PublicKeyString,
        mint: PublicKeyString,
        commitment: Optional[Commitment] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        return self.account_api.get_history(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            mint.public_key,
            commitment,
        )

    def get_token_accounts(
        self, account: PublicKeyString, mint: PublicKeyString, commitment: Optional[Commitment] = None
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        return self.account_api.get_token_accounts(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            mint.public_key,
            commitment,
        )

    def get_transaction(self, signature: str, commitment: Optional[Commitment] = None):
        commitment = self._get_commitment(commitment)

        return self.transaction_api.get_transaction(
            self.sdk_config["environment"], self.sdk_config["index"], signature, commitment=commitment
        )

    def make_transfer(
        self,
        owner: Keypair,
        destination: PublicKeyString,
        amount: str,
        mint: PublicKeyString,
        tx_type: TransactionType,
        reference_id: str,
        reference_type: str,
        sender_create: Optional[bool] = None,
        commitment: Optional[Commitment] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        destination = get_public_key(destination)
        sender_create = sender_create if sender_create is not None else False

        # FIXME: Use get_account_info to make behavior consistent with TypeScript SDK
        owner_token_account = get_associated_token_address(owner.public_key, PublicKey(mint.public_key))
        # We get the token account for the owner
        # The operation fails if the owner doesn't have a token account for this mint

        # FIXME: Use get_account_info to make behavior consistent with TypeScript SDK
        # We get the account info for the destination
        destination_token_account = get_associated_token_address(PublicKey(destination), PublicKey(mint.public_key))
        # The operation fails if the destination doesn't have a token account for this mint and senderCreate is not set
        # Derive the associated token address if the destination doesn't have a token account for this mint
        # and senderCreate is set
        # The operation fails if there is still no destination token account

        blockhash = self._get_block_hash_height(self.sdk_config["environment"], self.sdk_config["index"])

        tx = generate_make_transfer_transaction(
            add_memo=mint.add_memo,
            amount=amount,
            blockhash=blockhash["blockhash"],
            destination=destination,
            destination_token_account=destination_token_account,
            index=self.sdk_config["index"],
            mint_decimals=self.app_config["mint"]["decimals"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=mint.public_key,
            owner=owner,
            owner_token_account=owner_token_account,
            sender_create=sender_create,
            tx_type=tx_type,
        )

        request = MakeTransferRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=mint.public_key,
            reference_id=reference_id,
            reference_type=reference_type,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.transaction_api.make_transfer(request)

    def make_transfer_batch(
        self,
        owner,
        destinations,
        mint,
        tx_type,
        reference_id: str,
        reference_type: str,
        commitment: Optional[Commitment] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        # throw error if destinations is less than 1
        if len(destinations) < 1:
            raise Exception("At least 1 destination required")
        # throw error if destinations is greater than 15
        if len(destinations) > 15:
            raise Exception("Maximum number of destinations exceeded")

        # FIXME: Use get_account_info to make behavior consistent with TypeScript SDK
        owner_token_account = get_associated_token_address(owner.public_key, PublicKey(mint.public_key))
        # We get the token account for the owner
        # The operation fails if the owner doesn't have a token account for this mint

        # FIXME: Use get_account_info to make behavior consistent with TypeScript SDK
        # Get TokenAccount from destinations, keep track of missing ones

        # The operation fails if any of the destinations doesn't have a token account for this mint

        blockhash = self._get_block_hash_height(self.sdk_config["environment"], self.sdk_config["index"])

        tx = generate_make_transfer_batch_transaction(
            add_memo=mint.add_memo,
            blockhash=blockhash["blockhash"],
            destinations=destinations,
            index=self.sdk_config["index"],
            mint_decimals=self.app_config["mint"]["decimals"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=mint.public_key,
            owner=owner,
            owner_token_account=owner_token_account,
            tx_type=tx_type,
        )

        request = MakeTransferRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=mint.public_key,
            reference_id=reference_id,
            reference_type=reference_type,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.transaction_api.make_transfer(request)

    def request_airdrop(
        self,
        account: PublicKeyString,
        amount: str,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
    ):
        app_config = self._ensure_app_config()
        commitment = self._get_commitment(commitment)
        mint = self._get_app_mint(app_config, mint)

        request = RequestAirdropRequest(
            account=get_public_key(account),
            amount=amount,
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            mint=mint.public_key,
        )
        return self.airdrop_api.request_airdrop(request)

    def _api_base_options(self, configuration: Configuration, config):
        api_client = ApiClient(configuration)
        if config.get("headers") is not None:
            for header in config["headers"]:
                for key, value in header.items():
                    api_client.set_default_header(key, value)

        api_client.set_default_header("kinetic-environment", config["environment"])
        api_client.set_default_header("kinetic-index", config["index"])
        api_client.set_default_header("kinetic-user-agent", f"{NAME}/{VERSION}")
        return api_client

    def _ensure_app_config(self):
        if not self.app_config:
            raise Exception("App config not initialized")
        return self.app_config

    def _get_app_mint(self, app_config, mint: Optional[PublicKeyString] = None) -> AppConfigMint:
        if mint is None:
            mint = app_config.mint.public_key

        mint = get_public_key(mint)
        mint_found = list(filter(lambda item: item.get("public_key") == mint, app_config["mints"]))

        if len(mint_found) == 0:
            raise Exception("Mint not found")

        return mint_found[0]

    def _get_block_hash_height(self, environment: str, index: int):
        return self.transaction_api.get_latest_blockhash(environment, index)

    def _get_commitment(self, commitment: Optional[Commitment] = None) -> Commitment:
        if commitment is not None:
            return commitment
        if self.sdk_config["commitment"] is not None:
            return self.sdk_config["commitment"]
        return Commitment("Confirmed")
