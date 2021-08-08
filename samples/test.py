import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from pprint import pprint

from smaregipy import SmaregiPy
from smaregipy.account import Account
from smaregipy import pos

async def product_demo():
    pass
    try:
        product_list = await pos.ProductCollection().fetch_all()
        print('---product_list')
        pprint(product_list)
        # fetch product by id
        product = await pos.Product().id(1).fetch()
        print('---product')
        pprint(product)
    except Exception as e:
        pprint(e)

async def store_demo():
    try:
        store_ = pos.Store().id(1)
        store_2 = pos.Store().id(2)
        store_1 = await store_.fetch()
        print('---store_1 before')
        pprint(store_1)
        store_1.store_code = "test"
        store_1.point_condition.spend_rate = 1
        await store_1.save()
        print('---store_1 after')
        pprint(store_1)

        # fetch all stores, pick up a store, and update the store's store name
        all_stores = await pos.StoreCollection().fetch_all()
        print('---all stores')
        pprint(all_stores)
        print('---Collection is iterable')
        pprint(all_stores[0])

        print('---Collection also has "id" method for search by id from fetched data.')
        store_2 = all_stores.find(1)
        print('---use "save" method for updating or creating record. ')
        store_2.point_condition.point_use_division = False
        print('---store_2 updated')
        await store_2.save()
        pprint(store_2)

        # create store
        store_3 = pos.Store(
            store_name='store_3_created',
            store_code='store_3_created',
        )
        pprint(store_3)
        print('---store_3 created')
        await store_3.save()
        pprint(store_3)
        print('---and store_3 delete')
        await store_3.delete()

    except Exception as e:
        pprint(e)

async def transaction_demo():
    try:
        # fetch transaction detail by tansaction head
        transaction_list = await pos.TransactionCollection().fetch_list(
            **{
                'transaction_date_time-from': '2021-02-01T00:00:00+0900',
                'transaction_date_time-to': '2021-02-28T00:00:00+0900'
            },
            limit=5,
            page=2,
        )
        print('---transaction list')
        pprint(transaction_list)
        print('---transaction detail id 110')
        pprint(await transaction_list.find(110).details.fetch_all())

        # fetch transaction details having transaction head id 165
        transaction = await pos.Transaction().id(165).fetch()
        pprint(transaction)
        print('---transaction detail')
        pprint(transaction.details)
        # and fetch details having detail id 1
        pprint(transaction.details.find(1))


    except Exception as e:
        pprint(e)

async def create_transaction_detail_csv_demo():
    try:
        response = await pos.Transaction().details.create_csv(
            transactionDateTimeFrom='2021-02-01T00:00:00+0900',
            transactionDateTimeTo='2021-02-20T00:00:00+0900',
            callbackUrl=config.callback_uri
        )
        print('---transaction detail csv created')
        print(response)
    except Exception as e:
        pprint(e)

if __name__ == '__main__':
    from samples import config
    import asyncio
    SmaregiPy.init_by_dict(
        {
            'env_division': config.env_division,
            'contract_id': config.contract_id,
            'redirect_uri': config.redirect_uri,
            'smaregi_client_id': config.smaregi_client_id,
            'smaregi_client_secret': config.smaregi_client_secret
        }
    )

    account = Account.authorize(
        config.contract_id,
        [
            'pos.stores:read',
            'pos.stores:write',
            'pos.products:read',
            'pos.transactions:read',
        ]
    )

    if account is not None:
        print(account.access_token.token)

    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(
        store_demo(),
        product_demo(),
        transaction_demo(),
        create_transaction_detail_csv_demo(),
    )

    results = loop.run_until_complete(tasks)
    print(results)
