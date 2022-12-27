# pylint: disable=missing-function-docstring,missing-module-docstring
def get_solana_rpc_endpoint(endpoint: str):
    if endpoint == "devnet":
        return "devnet"
    if endpoint in ("mainnet", "mainnet-beta"):
        return "mainnet-beta"
    if endpoint.startswith("http"):
        return endpoint
    raise ValueError("Unknown http or https endpoint")
