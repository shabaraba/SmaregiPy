from smaregipy import SmaregiPy
from smaregipy.config import Config
from smaregipy.account import Account
from smaregipy import pos
import pdb

async def main():
    contract_id = 'sb_skc130x6' 
    smaregi_client_id = 'eaa4f2c64020b2d1e43577ec68b1f369'
    smaregi_client_secret = 'de611f8c486cfd24c29b6ab8486edf6d9c0f9d4838eb43f771616524ff2e2d18'
    SmaregiPy.init_by_dict(
        {
            'env_division': Config.ENV_DIVISION_DEVELOPMENT,
            'contract_id':contract_id,
            'smaregi_client_id':smaregi_client_id,
            'smaregi_client_secret':smaregi_client_secret
        }
    )

    account = Account.authorize(
        contract_id,
        ['pos.stores:read']
    )
    if account is not None:
        print(account.access_token.access_token)

    # get store by id
    print(await pos.Store.get(1))
    # get all store
    print(await pos.StoreCollection.get_all())


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(
        main(),
    )

    results = loop.run_until_complete(tasks)
    print(results)
