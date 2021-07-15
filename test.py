from smaregipy import SmaregiPy
from smaregipy.config import Config
from smaregipy.account import Account
import pdb


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
    print(account.access_token)

