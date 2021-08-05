from logging import Logger
from typing import TypeVar, Type
from . import account, pos
from .config import Config, init_config, init_auth_config, smaregi_config

__all__ = [
    'SmaregiPy',
    'smaregi_config',
    'pos',
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
        redirect_uri = dictionary.get('redirect_uri')
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
            (redirect_uri is None or isinstance(redirect_uri, str)) and
            (logger is None or isinstance(logger, Logger))
        ):
            init_config(
                env_division=env_division,
                contract_id=contract_id,
                redirect_uri=redirect_uri,
                client_id=smaregi_client_id,
                client_secret=smaregi_client_secret,
                access_token=access_token,
                logger=logger
            )
        if (
            (env_division is not None and isinstance(env_division, str)) and
            (smaregi_client_id is not None and isinstance(smaregi_client_id, str)) and
            (smaregi_client_secret is not None and isinstance(smaregi_client_secret, str)) and
            (redirect_uri is not None or isinstance(redirect_uri, str)) and
            (logger is None or isinstance(logger, Logger))
        ):
            init_auth_config(
                env_division=env_division,
                redirect_uri=redirect_uri,
                client_id=smaregi_client_id,
                client_secret=smaregi_client_secret,
                logger=logger
            )

    @classmethod
    def init_auth_by_dict(cls: Type[Smaregi], dictionary: dict) -> None:
        env_division = dictionary.get('env_division')
        redirect_uri = dictionary.get('redirect_uri')
        smaregi_client_id = dictionary.get('smaregi_client_id')
        smaregi_client_secret = dictionary.get('smaregi_client_secret')
        logger = dictionary.get('logger')
        if (
            (env_division is not None and isinstance(env_division, str)) and
            (redirect_uri is not None and isinstance(redirect_uri, str)) and
            (smaregi_client_id is not None and isinstance(smaregi_client_id, str)) and
            (smaregi_client_secret is not None and isinstance(smaregi_client_secret, str)) and
            (logger is None or isinstance(logger, Logger))
        ):
            global auth_config
            smaregi_config = init_auth_config(
                env_division=env_division,
                redirect_uri=redirect_uri,
                client_id=smaregi_client_id,
                client_secret=smaregi_client_secret,
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
