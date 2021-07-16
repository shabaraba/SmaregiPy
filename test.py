from pprint import pprint

from smaregipy import SmaregiPy
from smaregipy.config import Config
from smaregipy.account import Account
from smaregipy import pos
import pdb

async def product_demo():
    pass
    try:
        # get product by id
        product = await pos.Product.id(1).get()
        print('---product')
        pprint(product)
    except Exception as e:
        pprint(e)

async def store_demo():
    try:
        # get all stores, pick up a store, and update the store's store name
        all_stores = await pos.StoreCollection.get_all()
        updated_store = await all_stores.id(1).update(store_name="smaregipy")
        print('---store')
        pprint(updated_store)

    except Exception as e:
        pprint(e)

async def transaction_demo():
    try:
        # get transaction details having transaction head id 165
        transaction = await pos.Transaction.id(165).get(with_details='all')
        print('---transaction detail')
        pprint(transaction.details)
        # and get details having detail id 1
        pprint(transaction.details.id(1))
    except Exception as e:
        pprint(e)

if __name__ == '__main__':
    import asyncio
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
        [
            'pos.stores:read',
            'pos.stores:write',
            'pos.products:read',
            'pos.transactions:read',
        ]
    )

    if account is not None:
        print(account.access_token.access_token)

    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(
        store_demo(),
        product_demo(),
        transaction_demo(),
    )

    results = loop.run_until_complete(tasks)
    print(results)
