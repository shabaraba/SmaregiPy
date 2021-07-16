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
    uri_info: str
    uri_access: str
    uri_api: str
    uri_pos: str
    smargi_client_id: str
    smargi_client_secret: str
    contract_id: str
    redirect_uri: Optional[str]
    access_token: Optional[Account.AccessToken]
    logger: Optional[Logger]

    def __init__(
        self,
        env_division: str,
        contract_id: str,
        client_id: str,
        client_secret: str,
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
        if env_division is self.ENV_DIVISION_DEVELOPMENT:
            self.uri_access = 'https://id.smaregi.dev'
            self.uri_api = 'https://api.smaregi.dev'
        else:
            self.uri_access = 'https://id.smaregi.jp'
            self.uri_api = 'https://api.smaregi.jp'
        self.uri_info = self.uri_access + 'userinfo'
        self.uri_pos = self.uri_api + '/' + self.contract_id + '/pos'
        return self


def init_config(
    env_division: str,
    contract_id: str,
    client_id: str,
    client_secret: str,
    redirect_uri: Optional[str],
    access_token: Optional[Account.AccessToken] = None,
    logger: Optional[Logger] = None
    ) -> None:
    global smaregi_config
    smaregi_config = Config(
        env_division=env_division,
        contract_id=contract_id,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        access_token=access_token,
        logger=logger
    )


def update_access_token(access_token: Account.AccessToken) -> None:
    global smaregi_config
    smaregi_config.access_token = access_token

