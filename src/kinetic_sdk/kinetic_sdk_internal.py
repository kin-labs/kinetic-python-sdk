# pylint: disable=missing-function-docstring,missing-class-docstring,too-many-arguments,too-many-locals,fixme
"""Kinetic SDK Internal"""
from typing import Optional

import pybase64

from kinetic_sdk.generated import (
    AccountApi,
    AccountInfo,
    AirdropApi,
    ApiClient,
    AppApi,
    CloseAccountRequest,
    Commitment,
    Configuration,
    CreateAccountRequest,
    MakeTransferRequest,
    RequestAirdropRequest,
    TransactionApi,
)
from kinetic_sdk.helpers import (
    generate_create_account_transaction,
    generate_make_transfer_batch_transaction,
    generate_make_transfer_transaction,
    get_app_mint,
    get_public_key,
    get_token_address,
)
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models import NAME, VERSION, PublicKeyString, TransactionType


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
        reference: str,
    ):
        app_config = self._ensure_app_config()
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        request = CloseAccountRequest(
            account=get_public_key(account),
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            mint=app_mint.public_key,
            reference=reference,
        )

        return self.account_api.close_account(request)

    def create_account(
        self,
        owner: Keypair,
        commitment: Optional[Commitment] = None,
        mint: Optional[PublicKeyString] = None,
        reference: Optional[str] = None,
    ):
        app_config = self._ensure_app_config()
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        existing = self._find_token_account(account=owner.public_key, commitment=commitment, mint=app_mint.public_key)
        if existing is not None:
            raise Exception(f"Owner ${owner.public_key} already has a token account for mint ${app_mint.public_key}.")

        blockhash = self._get_blockhash_and_height(self.sdk_config["environment"], self.sdk_config["index"])

        owner_token_account = get_token_address(owner.public_key, app_mint.public_key)

        tx = generate_create_account_transaction(
            add_memo=app_mint.add_memo,
            blockhash=blockhash["blockhash"],
            index=self.sdk_config["index"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=app_mint.public_key,
            owner=owner,
            owner_token_account=owner_token_account,
        )

        request = CreateAccountRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=app_mint.public_key,
            reference=reference,
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
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        return self.account_api.get_account_info(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            app_mint.public_key,
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
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        return self.account_api.get_history(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            app_mint.public_key,
            commitment,
        )

    def get_kinetic_transaction(self, signature: Optional[str] = None, reference: Optional[str] = None):
        return self.transaction_api.get_kinetic_transaction(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            reference=reference or '',
            signature=signature or '',
        )

    def get_token_accounts(
        self, account: PublicKeyString, mint: PublicKeyString, commitment: Optional[Commitment] = None
    ):
        app_config = self._ensure_app_config()
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        return self.account_api.get_token_accounts(
            self.sdk_config["environment"],
            self.sdk_config["index"],
            get_public_key(account),
            app_mint.public_key,
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
        reference: str,
        sender_create: Optional[bool] = None,
        commitment: Optional[Commitment] = None,
    ):
        app_config = self._ensure_app_config()
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        destination = get_public_key(destination)
        sender_create = sender_create if sender_create is not None else False

        # We get the token account for the owner
        owner_token_account: Optional[str] = self._find_token_account(
            account=owner.public_key, commitment=commitment, mint=app_mint.public_key
        )
        # The operation fails if the owner doesn't have a token account for this mint
        if owner_token_account is None:
            raise Exception(f"Owner account doesn't exist for mint ${app_mint.public_key}.")

        # We get the account info for the destination
        destination_token_account: Optional[str] = self._find_token_account(
            account=destination, commitment=commitment, mint=app_mint.public_key
        )
        # The operation fails if the destination doesn't have a token account for this mint and sender_create is not set
        if destination_token_account is None and not sender_create:
            raise Exception(f"Destination account doesn't exist for mint ${app_mint.public_key}.")
        # Derive the associated token address if the destination doesn't have a token account for this mint
        # and sender_create is set
        sender_create_token_account: Optional[str] = None
        if destination_token_account is None and sender_create:
            sender_create_token_account = get_token_address(destination, app_mint.public_key)
        # The operation fails if there is still no destination token account
        if destination_token_account is None and sender_create_token_account is None:
            raise Exception("Destination token account not found.")

        blockhash = self._get_blockhash_and_height(self.sdk_config["environment"], self.sdk_config["index"])

        tx = generate_make_transfer_transaction(
            add_memo=app_mint.add_memo,
            amount=amount,
            blockhash=blockhash["blockhash"],
            destination=destination,
            destination_token_account=destination_token_account
            if destination_token_account
            else sender_create_token_account,
            index=self.sdk_config["index"],
            mint_decimals=self.app_config["mint"]["decimals"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=app_mint.public_key,
            owner=owner,
            owner_token_account=owner_token_account,
            sender_create=sender_create and sender_create_token_account is not None,
            tx_type=tx_type,
        )

        request = MakeTransferRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=app_mint.public_key,
            reference=reference,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.transaction_api.make_transfer(request)

    def make_transfer_batch(
        self,
        owner,
        destinations,
        mint,
        tx_type,
        reference: str,
        commitment: Optional[Commitment] = None,
    ):
        app_config = self._ensure_app_config()
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        # throw error if destinations is less than 1
        if len(destinations) < 1:
            raise Exception("At least 1 destination required")
        # throw error if destinations is greater than 15
        if len(destinations) > 15:
            raise Exception("Maximum number of destinations exceeded")

        # We get the token account for the owner
        owner_token_account: Optional[str] = self._find_token_account(
            account=owner.public_key, commitment=commitment, mint=app_mint.public_key
        )
        # The operation fails if the owner doesn't have a token account for this mint
        if owner_token_account is None:
            raise Exception(f"Owner account doesn't exist for mint ${app_mint.public_key}.")

        # FIXME: Use get_account_info to make behavior consistent with TypeScript SDK
        # Get TokenAccount from destinations, keep track of missing ones
        non_existing_destinations: list[str] = []
        destination_info: list[dict[str, str]] = []
        for item in destinations:
            destination: Optional[str] = self._find_token_account(
                account=item["destination"], commitment=commitment, mint=app_mint.public_key
            )
            if destination is None:
                non_existing_destinations.append(item["address"])
            else:
                destination_info.append(
                    {
                        "amount": item["amount"],
                        "destination": destination,
                    }
                )
        # The operation fails if any of the destinations doesn't have a token account for this mint
        if len(non_existing_destinations) > 0:
            raise Exception(
                f"Destination accounts {non_existing_destinations} "
                f"have no token account for mint ${app_mint.public_key}."
            )

        blockhash = self._get_blockhash_and_height(self.sdk_config["environment"], self.sdk_config["index"])

        tx = generate_make_transfer_batch_transaction(
            add_memo=app_mint.add_memo,
            blockhash=blockhash["blockhash"],
            destinations=destination_info,
            index=self.sdk_config["index"],
            mint_decimals=self.app_config["mint"]["decimals"],
            mint_fee_payer=self.app_config["mint"]["fee_payer"],
            mint_public_key=app_mint.public_key,
            owner=owner,
            owner_token_account=owner_token_account,
            tx_type=tx_type,
        )

        request = MakeTransferRequest(
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            last_valid_block_height=blockhash["last_valid_block_height"],
            mint=app_mint.public_key,
            reference=reference,
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
        app_mint = get_app_mint(app_config, mint)
        commitment = self._get_commitment(commitment)

        request = RequestAirdropRequest(
            account=get_public_key(account),
            amount=amount,
            commitment=commitment,
            environment=self.sdk_config["environment"],
            index=self.sdk_config["index"],
            mint=app_mint.public_key,
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

    def _find_token_account(self, account: str, commitment: Commitment, mint: str) -> Optional[str]:
        # We get the account info for the account
        account_info: AccountInfo = self.get_account_info(account, commitment, mint)

        # The operation fails when the account is a mint account
        if account_info.is_mint:
            raise Exception("Account is a mint account")

        # Find the token account for this mint
        # FIXME: we need to support the use case where the account has multiple accounts for this mint
        for token in account_info.tokens:
            if token.mint == mint:
                return token.account
        return None

    def _get_blockhash_and_height(self, environment: str, index: int):
        return self.transaction_api.get_latest_blockhash(environment, index)

    def _get_commitment(self, commitment: Optional[Commitment] = None) -> Commitment:
        if commitment is not None:
            return commitment
        if self.sdk_config["commitment"] is not None:
            return self.sdk_config["commitment"]
        return Commitment("Confirmed")
