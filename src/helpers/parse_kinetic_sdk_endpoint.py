def parse_kinetic_sdk_endpoint(endpoint: str):
    if endpoint == 'devnet':
        return 'https://devnet.kinetic.kin.org'
    elif endpoint == 'mainnet':
        return 'https://mainnet.kinetic.kin.org'
    elif endpoint.startswith('http'):
        return endpoint
    else:
        raise('Unknown http or https endpoint')
