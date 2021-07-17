import datetime
from typing import Optional, cast
from logging import Logger
import dataclasses

from smaregipy.entities.account import Account


@dataclasses.dataclass
class Config():
    ENV_DIVISION_DEVELOPMENT = 'DEV'
    ENV_DIVISION_PRODUCTION = 'PROD'

    env_division: str
    smargi_client_id: str
    smargi_client_secret: str
    uri_info: str
    uri_access: str
    uri_api: str
    uri_app_access_token: Optional[str]
    uri_pos: Optional[str]
    contract_id: Optional[str]
    redirect_uri: Optional[str]
    access_token: Optional[Account.AccessToken]
    logger: Optional[Logger]

    def __init__(
        self,
        env_division: str,
        client_id: str,
        client_secret: str,
        contract_id: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        access_token: Optional[Account.AccessToken] = None,
        logger: Optional[Logger] = None
    ):
        self.contract_id = contract_id
        self.redirect_uri = redirect_uri
        self.smaregi_client_id = client_id
        self.smaregi_client_secret = client_secret
        self.access_token = access_token
        self.logger = logger
        if env_division is not None:
            self.set_env(env_division)

    def set_env(self: 'Config', env_division: str) -> 'Config':
        self.env_division = env_division
        if env_division is self.ENV_DIVISION_PRODUCTION:
            self.uri_access = 'https://id.smaregi.jp'
            self.uri_api = 'https://api.smaregi.jp'
        else:
            self.uri_access = 'https://id.smaregi.dev'
            self.uri_api = 'https://api.smaregi.dev'
        self.uri_info = self.uri_access + 'userinfo'
        if self.contract_id is not None:
            self.uri_pos = "{endpoint}/{contract_id}/pos".format(
                endpoint=self.uri_api,
                contract_id=self.contract_id
            )
            self.uri_app_access_token = "{endpoint}/app/{contract_id}/token".format(
                endpoint=self.uri_access,
                contract_id=self.contract_id
            )
        return self


def init_config(
    env_division: str,
    client_id: str,
    client_secret: str,
    contract_id: Optional[str],
    redirect_uri: Optional[str],
    access_token: Optional[Account.AccessToken] = None,
    logger: Optional[Logger] = None
) -> None:
    global smaregi_config
    smaregi_config = Config(
        env_division=env_division,
        client_id=client_id,
        client_secret=client_secret,
        contract_id=contract_id,
        redirect_uri=redirect_uri,
        access_token=access_token,
        logger=logger
    )


def init_auth_config(
    env_division: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    logger: Optional[Logger] = None
) -> None:
    global smaregi_auth_config
    smaregi_auth_config = Config(
        env_division=env_division,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        logger=logger
    )


def update_access_token(access_token: Account.AccessToken) -> None:
    global smaregi_config
    smaregi_config.access_token = access_token

smaregi_config: 'Config' = Config(
    env_division=Config.ENV_DIVISION_DEVELOPMENT,
    client_id='client_id',
    client_secret='client_secret',
    contract_id='contract_id',
    redirect_uri='redirect_uri',
    access_token=None,
    logger=None
)

smaregi_auth_config: 'Config' = Config(
    env_division=Config.ENV_DIVISION_DEVELOPMENT,
    client_id='client_id',
    client_secret='client_secret',
    redirect_uri='redirect_uri',
    logger=None
)

