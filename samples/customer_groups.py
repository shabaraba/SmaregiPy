import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from pprint import pprint

from smaregipy import SmaregiPy
from smaregipy.account import Account
from smaregipy import pos

async def customer_groups_demo():
    try:
        print('---customer group list')
        customer_groups = await pos.CustomerGroupCollection().fetch_all()
        pprint(customer_groups)

        print('---customer group section list')
        customer_group_sections = await pos.CustomerGroupSectionCollection().fetch_all()
        pprint(customer_group_sections)

        print('---create customer group section')
        new_customer_group_section = await pos.CustomerGroupSection(
            customer_group_section_label='create_by_smargeipy'
        ).id(3).save()
        customer_group_sections = await pos.CustomerGroupSectionCollection().fetch_all()
        pprint(customer_group_sections)

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
            'pos.transactions:read',
            'pos.transactions:write',
        ]
    )

    if account is not None:
        print(account.access_token.token)

    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(
        customer_groups_demo(),
    )

    results = loop.run_until_complete(tasks)
    print(results)
