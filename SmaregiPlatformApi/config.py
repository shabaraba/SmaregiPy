import datetime
from typing import Optional, cast
from logging import Logger
import dataclasses

from SmaregiPlatformApi.entities.authorize import AccessToken


@dataclasses.dataclass
class Config():
    ENV_DIVISION_DEVELOPMENT = 'DEV'
    ENV_DIVISION_PRODUCTION = 'PROD'

    env_division: str
    usr_info: str
    uri_access: str
    uri_api: str
    uri_pos: str
    smargi_client_id: str
    smargi_client_secret: str
    access_token: AccessToken
    contract_id: str
    logger: Optional[Logger]

    def __init__(
        self,
        env_division: str,
        contract_id: str,
        client_id: str,
        client_secret: str,
        access_token: AccessToken,
        logger: Optional[Logger] = None
    ):
        self.contract_id = contract_id
        self.smaregi_client_id = client_id
        self.smaregi_client_secret = client_secret
        self.access_token = access_token
        self.logger = logger
        if env_division is not None:
            self.set_env(env_division)

    def set_env(self: 'Config', env_division: str) -> 'Config':
        self.env_division = env_division
        if env_division is self.ENV_DIVISION_DEVELOPMENT:
            self.uri_access = 'https://id.smaregi.dev'
            self.uri_api = 'https://api.smaregi.dev'
        else:
            self.uri_access = 'https://id.smaregi.jp'
            self.uri_api = 'https://api.smaregi.jp'
        self.uri_info = self.uri_access + 'userinfo'
        self.uri_pos = self.uri_api + '/' + self.contract_id + '/pos'
        return self

    def set_by_object(self: 'Config', updated_object: 'Config') -> 'Config':
        self.contract_id = updated_object.contract_id
        self.smaregi_client_id = updated_object.smaregi_client_id
        self.smaregi_client_secret = updated_object.smaregi_client_secret
        self.access_token = updated_object.access_token
        self.logger = updated_object.logger
        if updated_object.env_division is not None:
            self.set_env(updated_object.env_division)
        return self

    def set_by_dict(self: 'Config', dictionary: dict) -> 'Config':
        contract_id = dictionary.get('contract_id')
        if contract_id is not None and isinstance(str, contract_id):
            self.contract_id = contract_id
        smaregi_client_id = dictionary.get('smaregi_client_id')
        if smaregi_client_id is not None and isinstance(str, smaregi_client_id):
            self.smaregi_client_id = smaregi_client_id
        smaregi_client_secret = dictionary.get('smaregi_client_secret')
        if smaregi_client_secret is not None and isinstance(str, smaregi_client_secret):
            self.smaregi_client_secret = smaregi_client_secret
        access_token = dictionary.get('access_token')
        if access_token is not None and isinstance(AccessToken, access_token):
            self.access_token = access_token
        logger = dictionary.get('logger')
        if logger is not None and isinstance(Logger, logger):
            self.logger = logger
        env_division = dictionary.get('env_division')
        if env_division is not None and isinstance(str, env_division):
            self.set_env(env_division)

        return self

    def set_by_json_file(self: 'Config', file_path: str) -> 'Config':
        # TODO
        return self

    def set_by_toml_fyle(self: 'Config', file_path: str) -> 'Config':
        # TODO
        return self

    def set_by_yaml_file(self: 'Config', file_path: str) -> 'Config':
        # TODO
        return self


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
