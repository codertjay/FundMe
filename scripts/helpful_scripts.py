from brownie import network, accounts, config, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
FORKED_LOCAL_ENVIRONMENT = ['mainnet-fork','mainnet-fork-dev']


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or \
            network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    else:
        print('using this')
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    print(f"The network is {network.show_active()}")
    print(f'Deploying Mocks....')
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {'from': get_account()})
    print('Mocks Deployed')
