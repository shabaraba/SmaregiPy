from logging import Logger
from typing import Optional, TypeVar, Type
from . import account, pos, entities
from .config import Config, init_config, smaregi_config
from . import entities

__all__ = [
    'SmaregiPy',
    'AuthorizeApi',
    'smaregi_config',
    'TransactionsApi',
    'ProductsApi',
    'Store',
    'entities'
]

Smaregi = TypeVar('Smaregi', bound='SmaregiPy')

class SmaregiPy():
    @classmethod
    def init_by_object(cls: Type[Smaregi], updated_object: 'Config') -> None:
        global smaregi_config
        smaregi_config = updated_object

    @classmethod
    def init_by_dict(cls: Type[Smaregi], dictionary: dict) -> None:
        env_division = dictionary.get('env_division')
        contract_id = dictionary.get('contract_id')
        smaregi_client_id = dictionary.get('smaregi_client_id')
        smaregi_client_secret = dictionary.get('smaregi_client_secret')
        access_token = dictionary.get('access_token')
        logger = dictionary.get('logger')
        if (
            (env_division is not None and isinstance(env_division, str)) and
            (contract_id is not None and isinstance(contract_id, str)) and
            (smaregi_client_id is not None and isinstance(smaregi_client_id, str)) and
            (smaregi_client_secret is not None and isinstance(smaregi_client_secret, str)) and
            (access_token is None or isinstance(access_token, account.Account.AccessToken)) and
            (logger is None or isinstance(logger, Logger))
        ):
            global smaregi_config
            smaregi_config = init_config(
                env_division=env_division,
                contract_id=contract_id,
                client_id=smaregi_client_id,
                client_secret=smaregi_client_secret,
                access_token=access_token,
                logger=logger
            )


    def init_by_json_file(self: 'SmaregiPy', file_path: str) -> 'SmaregiPy':
        # TODO
        return self

    def init_config_by_toml_fyle(self: 'SmaregiPy', file_path: str) -> 'SmaregiPy':
        # TODO
        return self

    def init_config_by_yaml_file(self: 'SmaregiPy', file_path: str) -> 'SmaregiPy':
        # TODO
        return self
