# flake8: noqa: F841
# pylint: disable=missing-module-docstring
from solana.publickey import PublicKey

from kinetic_sdk import (
    AccountInfo,
    AppConfig,
    BalanceResponse,
    BalanceToken,
    ClusterType,
    Commitment,
    HistoryResponse,
    KineticSdk,
    RequestAirdropResponse,
    Transaction,
    TransactionStatus,
)
from kinetic_sdk.keypair import Keypair
from tests.fixtures import (
    ALICE_ACCOUNT,
    ALICE_KEYPAIR,
    ALICE_TOKEN_ACCOUNT,
    BOB_ACCOUNT,
    BOB_TOKEN_ACCOUNT,
    CHARLIE_ACCOUNT,
    DEFAULT_MINT,
    FEE_PAYER,
)

sdk = KineticSdk.setup(
    endpoint="http://localhost:3000",
    environment="local",
    index=1,
    headers=[{"kinetic-extra-header": "Test Header Value"}],
)


def test_get_balance():
    """Test getting balance of an account"""
    balance = sdk.get_balance(PublicKey(ALICE_ACCOUNT))
    assert isinstance(balance, BalanceResponse)
    assert isinstance(balance.balance, str)
    assert isinstance(balance.tokens, list)
    assert isinstance(balance.tokens[0], BalanceToken)
    assert isinstance(balance.mints, dict)
    assert isinstance(balance.mints[DEFAULT_MINT], str)


def test_get_app_config():
    """Test getting the app config"""
    app_config = sdk.config
    # print(app_config)
    assert isinstance(app_config, AppConfig)
    assert app_config["app"]["index"] == 1
    assert app_config["app"]["name"] == "App 1"
    assert app_config["environment"]["name"] == "local"
    assert app_config["environment"]["cluster"]["id"] == "solana-local"
    assert app_config["environment"]["cluster"]["name"] == "Solana Local"
    assert app_config["environment"]["cluster"]["type"] == ClusterType("Custom")
    assert app_config["mint"]["symbol"] == "KIN"
    assert app_config["mint"]["public_key"] == DEFAULT_MINT
    assert len(app_config["mints"]) == 2
    assert app_config["mints"][0].symbol == "KIN"
    assert app_config["mints"][0].public_key == DEFAULT_MINT


def test_get_explorer_url():
    """Test getting explorer url"""
    path = f"account/{ALICE_ACCOUNT}"
    url = sdk.get_explorer_url(path)
    expected = f"https://explorer.solana.com/{path}?cluster=custom&customUrl=http%3A%2F%2Flocalhost%3A8899"
    # print(url)
    assert url == expected


def test_get_history():
    """Test getting history of an account"""
    history = sdk.get_history(ALICE_ACCOUNT)
    # print(history)
    assert isinstance(history, list)
    assert isinstance(history[0], HistoryResponse)


def test_get_token_accounts():
    """Test getting token accounts of an account"""
    token_accounts = sdk.get_token_accounts(ALICE_ACCOUNT)
    # print(token_accounts)
    assert isinstance(token_accounts, list)


def test_request_airdrop():
    """Test requesting airdrop for an account"""
    airdrop = sdk.request_airdrop(ALICE_ACCOUNT, "100")
    # print(airdrop)
    assert isinstance(airdrop, RequestAirdropResponse)


def test_create_account():
    """Test creating an account"""
    kp = Keypair.random()
    created = sdk.create_account(kp)
    # print(created)
    assert isinstance(created, Transaction)
    assert created["errors"] == []
    assert created["amount"] is None
    assert str(created["commitment"]) == "Confirmed"
    assert created["destination"] is None
    assert created["fee_payer"] == FEE_PAYER
    assert created["mint"] == DEFAULT_MINT
    assert isinstance(created["status"], TransactionStatus)
    assert str(created["status"]) == "Committed"


def test_make_transfer():
    """Test making a transfer"""
    transfer = sdk.make_transfer(
        owner=ALICE_KEYPAIR,
        destination=BOB_ACCOUNT,
        amount=17,
    )
    assert isinstance(transfer, Transaction)
    assert transfer["errors"] == []
    assert transfer["amount"] == "17"
    assert transfer["commitment"] == "Confirmed"
    assert transfer["destination"] == BOB_TOKEN_ACCOUNT
    assert transfer["fee_payer"] == FEE_PAYER
    assert transfer["mint"] == DEFAULT_MINT
    assert isinstance(transfer["status"], TransactionStatus)
    assert transfer["status"] == TransactionStatus("Committed")
    assert transfer["source"] == ALICE_ACCOUNT


def test_make_transfer_batch():
    """Test making a batch transfer"""
    transfer_batch = sdk.make_transfer_batch(
        owner=ALICE_KEYPAIR,
        destinations=[{"destination": BOB_ACCOUNT, "amount": "12"}, {"destination": CHARLIE_ACCOUNT, "amount": "15"}],
    )
    # print(transfer_batch)
    assert isinstance(transfer_batch, Transaction)
    assert transfer_batch["errors"] == []
    assert transfer_batch["amount"] == "12"
    assert transfer_batch["commitment"] == "Confirmed"
    assert transfer_batch["destination"] == BOB_TOKEN_ACCOUNT
    assert transfer_batch["fee_payer"] == FEE_PAYER
    assert transfer_batch["mint"] == DEFAULT_MINT
    assert isinstance(transfer_batch["status"], TransactionStatus)
    assert transfer_batch["status"] == TransactionStatus("Committed")
    assert transfer_batch["source"] == ALICE_ACCOUNT


def test_get_transaction():
    """Test getting transaction"""
    new_transfer = sdk.make_transfer(
        owner=ALICE_KEYPAIR, destination=BOB_ACCOUNT, amount=1, commitment=Commitment("Finalized")
    )
    tx = sdk.get_transaction(signature=new_transfer["signature"])
    print(tx["signature"])


def test_sender_crete():
    """Test sender create"""
    destination = Keypair.random()
    tx = sdk.make_transfer(
        owner=ALICE_KEYPAIR,
        destination=destination.public_key,
        amount=1,
        commitment=Commitment("Finalized"),
        sender_create=True,
    )
    print(tx["signature"])


def test_get_account_info():
    """Test getting account info"""
    account_info = sdk.get_account_info(ALICE_ACCOUNT)
    # print(account_info)
    assert isinstance(account_info, AccountInfo)
    assert isinstance(account_info["is_mint"], bool)
    assert isinstance(account_info["is_owner"], bool)
    assert isinstance(account_info["is_token_account"], bool)
    assert isinstance(account_info["tokens"], list)
    assert account_info["tokens"][0].account == ALICE_TOKEN_ACCOUNT


def test_close_account():
    """Test closing an account"""
    kp = Keypair.random()
    sdk.create_account(kp, commitment=Commitment("Finalized"))
    tx = sdk.close_account(account=str(kp.public_key), commitment=Commitment("Finalized"))
    print(tx["signature"])
