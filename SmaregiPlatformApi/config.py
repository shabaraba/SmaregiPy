import dataclasses
import datetime

@dataclasses.dataclass
class Config():
    ENV_DIVISION_MOCK = 'MOCK'
    ENV_DIVISION_LOCAL = 'LOCAL'
    ENV_DIVISION_STAGING = 'STAGING'
    ENV_DIVISION_PRODUCTION = 'PROD'
    
    def __init__(self, env_division, client_id, client_secret, logger=None):
        if (env_division in (self.ENV_DIVISION_MOCK, self.ENV_DIVISION_LOCAL, self.ENV_DIVISION_STAGING)):
            self.uri_access = 'https://id.smaregi.dev'
            self.uri_api = 'https://api.smaregi.dev'
        else:
            self.uri_access = 'https://id.smaregi.jp'
            self.uri_api = 'https://api.smaregi.jp'

        self.smaregi_client_id = client_id
        self.smaregi_client_secret = client_secret
        self._uri_info = self.uri_access + 'userinfo'

        self.access_token = ''
        self.contract_id = ''

        self.logger = logger
