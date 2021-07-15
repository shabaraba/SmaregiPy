from urllib.parse import urlencode
from typing import TypeVar, Type, Tuple, List, Union, cast
import datetime
import pytz

import requests

from . import config
from .base_api import BaseIdentificationApi
from .entities import ErrorResponse
from .entities.account import Account as AccountEntity


AccountType = TypeVar('AccountType', bound='Account')

class Account(AccountEntity, BaseIdentificationApi):
    @classmethod
    def authorize(cls: Type[AccountType], contract_id: str, scope_list: List[str]) -> Union['Account', None]:
        url = "{endpoint}/app/{contract_id}/token".format(
            endpoint=config.smaregi_config.uri_access,
            contract_id=contract_id
        )
        headers = cls._get_header()
        scope_string = " ".join(scope_list)
        body = {
            'grant_type': 'client_credentials',
            'scope': scope_string
        }
        response = requests.post(url, headers=headers, data=urlencode(body))
        result = response.json()

        if response.status_code != 200:
            error_response = ErrorResponse(result)
            return None
        return Account(
            contract_id=contract_id,
            access_token=cast(str, result.get('access_token')),
            access_token_expiration_datetime=datetime.datetime.now(pytz.timezone('Asia/Tokyo')) + datetime.timedelta(seconds=result['expires_in'])
        )

class AuthorizeApi(BaseIdentificationApi):
    def __init__(self, redirect_uri):
        self.redirect_uri = redirect_uri
        self.csrf = 'rundomStringForProdcution'
        self.uri_auth = config.smaregi_config.uri_access + '/authorize'
        self.uri_info = config.smaregi_config.uri_access + '/userinfo'

    def authorize(self):
        query = {
            'response_type': 'code',
            'client_id': config.smaregi_config.smaregi_client_id,
            'scope': 'openid',
            'state': self.csrf,
            'redirect_uri': self.redirect_uri
        }
        params = urlencode(query)
        return f'{self.uri_auth}?{params}'
        # return redirect(f'{self.uriAuth}?{params}')

    def get_user_info(self, code, state):
        user_access_token = self._get_user_access_token(code)
        access_token = user_access_token.access_token
        info_header = {
            'Authorization': 'Bearer ' + access_token
        }

        r_post = requests.post(self.uri_info, headers=info_header).json()
        return UserInfo(r_post)

    def get_access_token(self, contract_id, scope_list):
        url = smaregi_config.uri_access + '/app/' + contract_id + '/token'
        headers = self._get_header()
        scope_string = " ".join(scope_list)
        body = {
            'grant_type': 'client_credentials',
            'scope': scope_string
        }
        r_post = requests.post(url, headers=headers, data=urlencode(body))
        r_post = r_post.json()

        access_token = r_post['access_token']
        expiration_datetime = datetime.datetime.now(pytz.timezone('Asia/Tokyo')) + datetime.timedelta(seconds=r_post['expires_in'])
        return AccessToken(access_token, expiration_datetime)

    def _get_user_access_token(self, code):
        headers = self._get_header()
        body = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
        }
        result = requests.post(self.uri_auth + '/token', headers=headers, data=urlencode(body))
        result = result.json()

        return UserAccessToken(result['access_token'])
