import base64
import requests
import json
from logging import Logger
from urllib.parse import urlencode
import asyncio

from .entities import ErrorResponse
from . import config

from typing import (
    Any,
    Dict,
    Tuple,
    Optional,
    List,
    TypeVar,
    Type
)


class BaseApi():
    config: 'Config'
    def __init__(self, **kwargs):
        pass

    @staticmethod
    def _get_base64_encode(string):
        return base64.b64encode(string)

    def set_config(self, config: 'Config'):
        self.config = config
        return self


class BaseIdentificationApi(BaseApi):
    @staticmethod
    def _get_header():
        authorization_string = (
            config.smaregi_config.smaregi_client_id +
            ":" +
            config.smaregi_config.smaregi_client_secret
        ).encode()
        encoded_string = BaseIdentificationApi._get_base64_encode(authorization_string)
        base64encoded = "Basic " + str(encoded_string).split("'")[1]
        return {
            'Authorization': base64encoded,
            'Content-Type': 'application/x-www-form-urlencoded',
        }


Collection = TypeVar('Collection', bound='BaseServiceCollectionApi')

class BaseServiceApi(BaseApi):
    UNIT_NAME: str
    
    def __init__(self, *args):
        pass

    @staticmethod
    def _get_header():
        auth = "Bearer " + config.smaregi_config.access_token.access_token
        return {
            'Authorization': auth,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    @staticmethod
    def _get_query(field=None, sort=None, where_dict=None):
        body = {
            'limit': 1000,
            'page': 1
        }
        if (field is not None):
            body.update({
                'fields': field
            })
        if (sort is not None):
            body.update({
                'sort': sort
            })
        if (where_dict is not None):
            body.update(where_dict)

        return body

    @staticmethod
    def _get_query_for_detail(field=None, sort=None, where_dict=None, **kwargs):
        body = {
        }
        if (field is not None):
            body.update({
                'fields': field
            })
        if (sort is not None):
            body.update({
                'sort': sort
            })
        if (where_dict is not None):
            body.update(where_dict)
        body.update(kwargs)

        return body

    @staticmethod
    def _api_get(uri: str, header: Dict, body: Dict) -> Tuple[int, Any]:
        """APIを実施します
        link、pageがある場合、すべて実施してデータを結合します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.get(uri, headers=header, params=urlencode(body))
        result_list = response.json()
        if response.status_code != 200:
            error_response = ErrorResponse(result_list)
            return (response.status_code, error_response)

        while (('link' in response.headers) and ('next' in response.links)):
            print(response.links)
            uriNext = response.links['next']['url']
            response = requests.get(uriNext, headers=header)
            if response.status_code != 200:
                error_response = ErrorResponse(result_list)
                return (response.status_code, error_response)
            result_list.extend(response.json())

        return (response.status_code, result_list)

    def _api_post(self, uri: str, header: Dict, body: Dict) -> Tuple[int, Any]:
        """POSTのAPIを実施します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.post(uri, headers=header, data=json.dumps(body))
        result = response.json()
        if response.status_code != 200:
            error_response = ErrorResponse(result)
            return (response.status_code, error_response)

        return (response.status_code, result)


class BaseServiceCollectionApi(BaseServiceApi):
    UNIT_NAME: str

    def __init__(self, *args):
        pass

    @classmethod
    async def get_all(cls: Type[Collection], **kwargs) -> Collection:
        uri = "{endpoint}/{unit_name}".format(
            endpoint=config.smaregi_config.uri_pos,
            unit_name=cls.UNIT_NAME
        )
        header = cls._get_header()
        body = cls._get_query(
            field=None,
            sort=None,
            where_dict=kwargs
        )

        response = BaseServiceRecordApi._api_get(uri, header, body)
        if response[0] != 200:
            raise response[1]
        response_data = response[1]

        return cls(response_data)

    @classmethod
    async def get_list(cls:Type[Collection], limit: Optional[int] = None, offset: Optional[int] = None, **kwargs) -> Collection:
        uri = "{endpoint}/{unit_name}/{unit_id}".format(
            endpoint=config.smaregi_config.uri_pos,
            unit_name=cls.UNIT_NAME,
            unit_id=id
        )
        header = cls._get_header()
        body = cls._get_query_for_detail(
            field=None,
            sort=None,
            where_dict=kwargs
        )

        response = BaseServiceRecordApi._api_get(uri, header, body)
        if response[0] != 200:
            raise response[1]
        response_data = response[1]

        return cls(response_data)


Unit = TypeVar('Unit', bound='BaseServiceRecordApi')

class BaseServiceRecordApi(BaseServiceApi):
    UNIT_NAME: str

    def __init__(self, *args):
        pass

    @classmethod
    async def get(cls: Type[Unit], id: int,  **kwargs) -> Unit:
        uri = "{endpoint}/{unit_name}/{unit_id}".format(
            endpoint=config.smaregi_config.uri_pos,
            unit_name=cls.UNIT_NAME,
            unit_id=id
        )
        header = cls._get_header()
        body = cls._get_query_for_detail(
            field=None,
            sort=None,
            where_dict=kwargs
        )

        response = BaseServiceRecordApi._api_get(uri, header, body)
        if response[0] != 200:
            raise response[1]
        response_data = response[1]

        return cls(response_data)

    @classmethod
    async def create(cls: Type[Unit], **kwargs) -> Unit:
        result = cls(kwargs)
        return result

    async def save(self: 'BaseServiceRecordApi', **kwargs) -> 'BaseServiceRecordApi':
        return self

    async def update(self: 'BaseServiceRecordApi', **kwargs) -> 'BaseServiceRecordApi':
        return self

    async def delete(self: 'BaseServiceRecordApi', **kwargs) -> bool:
        return True

