import datetime
from typing import Optional
from logging import Logger
import dataclasses

from SmaregiPlatformApi.entities.authorize import AccessToken


@dataclasses.dataclass
class Config():
    ENV_DIVISION_DEVELOPMENT = 'DEV'
    ENV_DIVISION_PRODUCTION = 'PROD'

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
            self.set_uri_by_env(env_division)

    def set_uri_by_env(self: 'Config', env_division: str) -> 'Config':
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
        self.env_division = updated_object.env_division
        self.smaregi_client_id = updated_object.smaregi_client_id
        self.smaregi_client_secret = updated_object.smaregi_client_secret
        self.uri_info = updated_object.uri_info
        self.uri_access = updated_object.uri_access
        self.env_division = updated_object.env_division
        return self

    def set_by_dict(self: 'Config', dictionary: dict) -> 'Config':
        # TODO
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
