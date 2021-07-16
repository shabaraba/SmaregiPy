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
        product = await pos.Product().id(1).get()
        print('---product')
        pprint(product)
    except Exception as e:
        pprint(e)

async def store_demo():
    try:
        # get all stores, pick up a store, and update the store's store name
        all_stores = await pos.StoreCollection().get_all()
        updated_store = await all_stores.id(1).update(store_name="smaregipy")
        print('---store')
        pprint(updated_store)

    except Exception as e:
        pprint(e)

async def transaction_demo():
    try:
        # get transaction details having transaction head id 165
        transaction = await pos.Transaction().id(165).get(with_details='all')
        print('---transaction detail')
        pprint(transaction.details)
        # and get details having detail id 1
        pprint(transaction.details.id(1))

        # get transaction detail by tansaction head
        transaction_list = await pos.TransactionCollection().get_list(limit=5, page=2)

        pdb.set_trace()
        print('---transaction list')
        pprint(transaction_list)
        print('---transaction detail id 7')
        pprint(await transaction_list.id(7).details.get_all())

    except Exception as e:
        pprint(e)

async def create_transaction_detail_csv_demo():
    try:
        response = await pos.Transaction().details.create_csv(
            transactionDateTimeFrom='2021-02-01T00:00:00+0900',
            transactionDateTimeTo='2021-02-20T00:00:00+0900',
            callbackUrl='https://webhook.site/a014e761-9c20-4d4e-b104-f03faeeec087'
        )
        print('---transaction detail csv created')
        print(response)
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
        create_transaction_detail_csv_demo(),
    )

    results = loop.run_until_complete(tasks)
    print(results)
