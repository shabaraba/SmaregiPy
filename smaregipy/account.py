from urllib.parse import urlencode
from typing import TypeVar, Type, Tuple, List, Union, cast
import datetime
import pytz

import requests

from . import config
from .base_api import BaseIdentificationApi
from .exceptions import ResponseException
from .entities.account import Account as AccountEntity


AccountType = TypeVar('AccountType', bound='Account')

class Account(AccountEntity, BaseIdentificationApi):
    @classmethod
    def authentication_uri(cls: Type[AccountType]) -> str:
        uri = "{endpoint}/authorize".format(endpoint=config.smaregi_auth_config.uri_access)
        query = {
            'response_type': 'code',
            'client_id': config.smaregi_auth_config.smaregi_client_id,
            'scope': 'openid',
            'state': 'todo_create_random_str',
            'redirect_uri': config.smaregi_auth_config.redirect_uri,
        }
        params = urlencode(query)
        return "{endpoint}?{params}".format(
            endpoint=uri,
            params=params
        )

    @classmethod
    def authenticate(cls: Type[AccountType], code: str, state: str) -> 'Account':
        user_access_token = cls.__get_user_access_token(code)
        access_token = user_access_token.access_token
        info_header = {
            'Authorization': 'Bearer ' + access_token
        }
        uri = config.smaregi_auth_config.uri_info

        response = requests.post(uri, headers=info_header).json()
        return Account(
            contract_id=response['contract']['id'],
            sub=response['sub'],
            is_owner=response['contract']['is_owner'],
        )

    @classmethod
    def authorize(cls: Type[AccountType], contract_id: str, scope_list: List[str]) -> 'Account':
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
        try:
            response = requests.post(url, headers=headers, data=urlencode(body))
        except ResponseException as e:
            raise e

        result = response.json()
        account = Account(
            contract_id=contract_id,
            access_token=cast(str, result.get('access_token')),
            access_token_expiration_datetime=datetime.datetime.now(pytz.timezone('Asia/Tokyo')) + datetime.timedelta(seconds=result['expires_in'])
        )

        config.update_access_token(account.access_token)

        return account

    @classmethod
    def __get_user_access_token(cls, code) -> AccountEntity.UserAccessToken:
        headers = BaseIdentificationApi._get_header()
        body = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': config.smaregi_config.redirect_uri,
        }
        uri = "{endpoint}/authorize/token".format(
            endpoint=config.smaregi_config.uri_acces
        )
        result = requests.post(uri, headers=headers, data=urlencode(body))
        result = result.json()

        return Account.UserAccessToken(result['access_token'])
