# pylint: disable=missing-function-docstring,missing-module-docstring
from typing import Optional

from kinetic_sdk.generated import AppConfig, AppConfigMint
from kinetic_sdk.helpers.get_public_key import get_public_key
from kinetic_sdk.models import PublicKeyString


def get_app_mint(app_config: AppConfig, mint: Optional[PublicKeyString] = None) -> AppConfigMint:
    if mint is None:
        mint = app_config.mint.public_key

    mint = get_public_key(mint)
    mint_found = list(filter(lambda item: item.get("public_key") == mint, app_config["mints"]))

    if len(mint_found) == 0:
        raise Exception("Mint not found")

    return mint_found[0]
