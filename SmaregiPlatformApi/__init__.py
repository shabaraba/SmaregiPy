import datetime

from .authorize import AuthorizeApi
from .config import Config
from .pos import (
    TransactionsApi,
    ProductsApi,
    StoresApi
)
import SmaregiPlatformApi.entities as entities

__all__ = [
    'AuthorizeApi',
    'Config',
    'smaregi_config',
    'TransactionsApi',
    'ProductsApi',
    'StoresApi',
    'entities'
]

__version__ = '0.1.1'


smaregi_config = Config(
    Config.ENV_DIVISION_DEVELOPMENT,
    'contract_id',
    'client_id',
    'client_secret',
    entities.AccessToken(
        'access_token',
        datetime.datetime.now()
    )
)
