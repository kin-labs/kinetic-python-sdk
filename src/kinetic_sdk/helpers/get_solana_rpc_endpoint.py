def get_solana_rpc_endpoint(endpoint: str):
    if endpoint == 'devnet':
        return 'devnet'
    elif endpoint == 'mainnet' or endpoint=='mainnet-beta':
        return 'mainnet-beta'
    elif endpoint.startswith('http'):
        return endpoint
    else:
        raise 'Unknown http or https endpoint'
