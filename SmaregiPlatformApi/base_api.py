import base64
import requests
import json
import time
import logging
from urllib.parse import urlencode

from .entities import ErrorResponse
from .config import Config

from typing import (
    Any,
    Dict,
    Tuple,
)


class BaseApi():
    def __init__(self, config: 'Config'):
        self.config = config
        # self.logger = self.config.logger

    def _get_base64_encode(self, string):
        return base64.b64encode(string)


class BaseIdentificationApi(BaseApi):
    def _show_authorization_string(self):
        return (
            self.config.smaregi_client_id +
            ":" +
            self.config.smaregi_client_secret
        ).encode()

    def _get_smaregi_auth(self):
        string = self._show_authorization_string()
        base = self._get_base64_encode(string)
        return "Basic " + str(base).split("'")[1]

    def _get_header(self):
        return {
            'Authorization': self._get_smaregi_auth(),
            'Content-Type': 'application/x-www-form-urlencoded',
        }


class BaseServiceApi(BaseApi):
    def _show_authorization_string(self):
        return self.config.access_token.access_token

    def _get_smaregi_auth(self):
        string = self._show_authorization_string()
        return "Bearer " + string

    def _get_header(self):
        return {
            'Authorization': self._get_smaregi_auth(),
            'Content-Type': 'application/x-www-form-urlencoded',        
        }

    def _get_query(self, field=None, sort=None, where_dict=None):
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

    def _get_query_for_detail(self, field=None, sort=None, where_dict=None, **kwargs):
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

    def _get_request_body():
        body = {}

    def _api_get(self, uri: str, header: Dict, body: Dict) -> Tuple[int, Any]:
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
            tuple[int, any]: status_code, response の tuple
        """
        response = requests.post(uri, headers=header, data=json.dumps(body))
        result = response.json()
        if response.status_code != 200:
            error_response = ErrorResponse(result)
            return (response.status_code, error_response)

        return (response.status_code, result)
