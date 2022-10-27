from kinetic_sdk_generated.api.account_api import AccountApi
from kinetic_sdk_generated.api.airdrop_api import AirdropApi
from kinetic_sdk_generated.api.app_api import AppApi
from kinetic_sdk_generated.api.transaction_api import TransactionApi
from kinetic_sdk_generated.model.create_account_request import CreateAccountRequest
from kinetic_sdk_generated.model.make_transfer_request import MakeTransferRequest
from kinetic_sdk_generated.model.request_airdrop_request import RequestAirdropRequest
from kinetic_sdk_generated.model.commitment import Commitment
from kinetic_sdk_generated import ApiClient
from kinetic_sdk_generated import Configuration

from kinetic_sdk.helpers.generate_create_account_transaction import generate_create_account_transaction
from kinetic_sdk.helpers.generate_make_transfer_transaction import generate_make_transfer_transaction
from kinetic_sdk.helpers.get_public_key import get_public_key

from kinetic_sdk.models.public_key_string import PublicKeyString
from kinetic_sdk.models.transaction_type import TransactionType
from kinetic_sdk.models.keypair import Keypair


import pybase64


class KineticSdkInternal(object):

    def __init__(self, config):
        configuration = Configuration(host=config['endpoint'])
        api_client = ApiClient(configuration)
        self.account_api = AccountApi(api_client)
        self.airdrop_api = AirdropApi(api_client)
        self.app_api = AppApi(api_client)
        self.transaction_api = TransactionApi(api_client)
        self.environment = config['environment']
        self.index = config['index']
        self.app_config = self.app_api.get_app_config(self.environment, self.index)

    def create_account(self, owner: Keypair, mint: str, commitment):
        blockhash = self._prepare_transaction(self.environment, self.index)
        mint = self._get_app_mint(self.app_config, mint)

        tx = generate_create_account_transaction(
            add_memo=False,
            app_index=self.index,
            recent_blockhash=blockhash['blockhash'],
            mint_fee_payer=self.app_config['mint']['fee_payer'],
            mint_public_key=mint,
            owner=owner,
        )

        create_account_request = CreateAccountRequest(
            commitment=commitment,
            environment=self.environment,
            index=self.index,
            last_valid_block_height=blockhash['last_valid_block_height'],
            mint=mint,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.account_api.create_account(create_account_request)

    def get_app_config(self, environment, index):
        return self.app_api.get_app_config(environment, index)

    def get_balance(self, account: PublicKeyString):
        account = get_public_key(account)
        return self.account_api.get_balance(self.environment, self.index, account)

    def get_explorer_url(self, path: str):
        return self.app_config['environment']['explorer'].replace('{path}', path)

    def get_history(self, account: PublicKeyString, mint: PublicKeyString):
        mint = self._get_app_mint(self.app_config, mint)
        account = get_public_key(account)
        return self.account_api.get_history(self.environment, self.index, account, mint)

    def get_token_accounts(self, account: PublicKeyString, mint: PublicKeyString):
        mint = self._get_app_mint(self.app_config, mint)
        account = get_public_key(account)
        return self.account_api.get_token_accounts(self.environment, self.index, account, mint)

    def get_transaction(self, signature: str):
        return self.transaction_api.get_transaction(self.environment, self.index, signature)

    def make_transfer(
        self,
        owner: Keypair,
        destination: PublicKeyString,
        amount: str,
        mint: PublicKeyString,
        tx_type: TransactionType,
        commitment: Commitment
    ):
        blockhash = self._prepare_transaction(self.environment, self.index)
        mint = self._get_app_mint(self.app_config, mint)
        destination = get_public_key(destination)

        tx = generate_make_transfer_transaction(
            amount=amount,
            add_memo=False,
            app_index=self.index,
            recent_blockhash=blockhash['blockhash'],
            destination=destination,
            decimals=self.app_config['mint']['decimals'],
            mint_fee_payer=self.app_config['mint']['fee_payer'],
            mint_public_key=mint,
            source=owner,
        )

        make_transfer_request = MakeTransferRequest(
            commitment=commitment,
            environment=self.environment,
            index=self.index,
            last_valid_block_height=blockhash['last_valid_block_height'],
            mint=mint,
            reference_id=None,
            reference_type=None,
            tx=pybase64.b64encode_as_string(tx),
        )

        return self.transaction_api.make_transfer(make_transfer_request)

    def request_airdrop(self, account: PublicKeyString, amount: str, mint: str, commitment: Commitment):
        mint = self._get_app_mint(self.app_config, mint)
        account = get_public_key(account)
        request_airdrop_request = RequestAirdropRequest(
            account=account,
            commitment=commitment,
            environment=self.environment,
            index=self.index,
            mint=mint,
            amount=amount,
        )
        return self.airdrop_api.request_airdrop(request_airdrop_request)

    def _prepare_transaction(self, environment, index):
        return self.transaction_api.get_latest_blockhash(environment, index)


    def _get_app_mint(self, app_config, mint: PublicKeyString):
        if mint == None:
            mint = app_config.mint.public_key

        mint = get_public_key(mint)
        mint_found = list(filter(lambda item: item.get("public_key") == mint, app_config['mints']))

        if len(mint_found) == 0:
            raise "Mint not found"

        return mint
