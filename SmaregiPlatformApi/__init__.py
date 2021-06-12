import datetime

from .authorize import AuthorizeApi
from .config import Config
from .pos import (
    TransactionsApi,
    ProductsApi,
    StoresApi
)
from .entities import *

__all__ = [
    'AuthorizeApi',
    'Config',
    'smaregi_config',
    'TransactionsApi',
    'ProductsApi',
    'StoresApi'
]

__version__ = '0.1.0'


smaregi_config = Config(
    Config.ENV_DIVISION_DEVELOPMENT,
    'contract_id',
    'client_id',
    'client_secret',
    AccessToken(
        'access_token',
        datetime.datetime.now()
    )
)
