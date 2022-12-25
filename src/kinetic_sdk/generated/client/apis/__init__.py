# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from kinetic_sdk.generated.client.api.account_api import AccountApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from kinetic_sdk.generated.client.api.account_api import AccountApi
from kinetic_sdk.generated.client.api.airdrop_api import AirdropApi
from kinetic_sdk.generated.client.api.app_api import AppApi
from kinetic_sdk.generated.client.api.transaction_api import TransactionApi
