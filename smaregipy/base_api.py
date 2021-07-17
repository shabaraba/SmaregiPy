import base64
import requests
import json
import copy
from logging import Logger
from urllib.parse import urlencode
import asyncio

from typing import (
    Any,
    Dict,
    Tuple,
    Optional,
    List,
    TypeVar,
    Type,
    Union
)

from .exceptions import ResponseException
from . import config
from .entities.base_entity import BaseEntity


class BaseApi():
    class Response():
        KEY_STATUS = 0  # api response array key 0 is status code
        KEY_DATA = 1  # api resposne array key 1 is response data
        KEY_ERROR = 1  # when error, api resposne array key 1 is error message

        STATUS_SUCCESS = 200
        STATUS_ACCEPTED = 202
        STATUS_BAD_REQUEST_ERROR = 400
        STATUS_UNAUTHORIZED_ERROR = 401
        STATUS_FORBIDDEN_ERROR = 403
        STATUS_NOT_FOUND_ERROR = 404
        STATUS_FATAL_ERROR = 503

    @staticmethod
    def _get_base64_encode(string):
        return base64.b64encode(string)


class BaseIdentificationApi(BaseApi):
    @staticmethod
    def _get_header():
        authorization_string = (
            config.smaregi_auth_config.smaregi_client_id +
            ":" +
            config.smaregi_auth_config.smaregi_client_secret
        ).encode()
        encoded_string = BaseIdentificationApi._get_base64_encode(authorization_string)
        base64encoded = "Basic " + str(encoded_string).split("'")[1]
        return {
            'Authorization': base64encoded,
            'Content-Type': 'application/x-www-form-urlencoded',
        }


BaseService = TypeVar('BaseService', bound='BaseServiceApi')

class BaseServiceApi(BaseApi):
    PATH_PARAMS: List[str]

    path_params_id_list: List[int]


    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def _get_uri(
        cls: Type[BaseService],
        path_params: Optional[Dict[str, Optional[str]]] = None
    ) -> str:
        return "{endpoint}/{path_list}".format(
            endpoint=config.smaregi_config.uri_pos,
            path_list="/".join(
                [
                    "{path}{params}".format(
                        path=k,
                        params="/{}".format(v) if v is not None else ""
                    ) for k, v in path_params.items()
                ]
            ) if path_params is not None else "",
        )

    @staticmethod
    def _get_header():
        auth = "Bearer " + config.smaregi_config.access_token.access_token
        return {
            'Authorization': auth,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    @staticmethod
    def _get_query(
        field: Optional[List[str]] = None,
        sort: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        where_dict: Optional[Dict[Any, str]] = None
    ):
        body = { }
        if (field is not None):
            body.update({
                'fields': ','.join(field)
            })
        if (sort is not None):
            body.update({
                'sort': ','.join(' '.join(["{params}:{ascending}".format(k, v) for k, v in sort.items()]))
            })
        if (limit is not None and page is not None):
            body.update({
                'limit': limit,
                'page': page
            })
        if (where_dict is not None):
            body.update(where_dict)

        return body

    @staticmethod
    def _api_get(uri: str, header: Dict, body: Dict, all: bool = False) -> Tuple[int, Any]:
        """GETのAPIを実施します
        link、pageがある場合、すべて実施してデータを結合します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.get(uri, headers=header, params=urlencode(body))
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )
        result_list = response.json()

        if all is True:
            while (('link' in response.headers) and ('next' in response.links)):
                print(response.links)
                uriNext = response.links['next']['url']
                response = requests.get(uriNext, headers=header)
                if response.status_code not in [
                    BaseApi.Response.STATUS_SUCCESS,
                    BaseApi.Response.STATUS_ACCEPTED,
                ]:
                    raise ResponseException(
                        response.json()
                    )
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
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )

        return (response.status_code, result)

    def _api_patch(self, uri: str, header: Dict, body: Dict) -> Tuple[int, Any]:
        """PATCHのAPIを実施します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.patch(uri, headers=header, data=json.dumps(body))
        result = response.json()
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )

        return (response.status_code, result)


Collection = TypeVar('Collection', bound='BaseServiceCollectionApi')


class BaseServiceCollectionApi(BaseServiceApi):
    RECORD_NAME: str

    def __init__(
        self,
        data: List = [],
        path_params: Dict[str, Union[str, None]] = {},
    ) -> None:
        self.records:Dict[str, Any]
        self.path_params: Dict[str, Union[str, None]] = copy.deepcopy(path_params)
        self.path_params[self.RECORD_NAME] = None

    def __new__(
        cls: Type[BaseService],
        *args,
        fetched_data: bool = True,
        **kwargs
    ) -> 'BaseServiceCollectionApi':
        if fetched_data is True:
            # APIでデータを取得した場合のみentityのinitでインスタンス化する
            self = super().__new__(cls)
        else:
            # 取得していない場合はserviceApiのinitでインスタンス化する
            self = BaseServiceApi.__new__(cls)
        self.path_params_id_list = []
        return self

    def __repr__(self) -> str:
        return str(self.records)

    async def get_all(
        self: 'BaseServiceCollectionApi',
        field: Optional[List] = None,
        sort: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> 'BaseServiceCollectionApi':
        uri = self._get_uri(self.path_params)
        header = self._get_header()
        body = self._get_query(
            field=field,
            sort=sort,
            where_dict=kwargs
        )

        try:
            response = self._api_get(uri, header, body)
        except ResponseException as e:
            raise e
        response_data = response[self.Response.KEY_DATA]

        return self.__class__(response_data, path_params=self.path_params)

    async def get_list(
        self: 'BaseServiceCollectionApi',
        field: Optional[List] = None,
        sort: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        **kwargs
    ) -> 'BaseServiceCollectionApi':
        uri = self._get_uri(self.path_params)
        header = self._get_header()
        body = self._get_query(
            field=field,
            sort=sort,
            limit=limit,
            page=page,
            where_dict=kwargs
        )

        try:
            response = self._api_get(uri, header, body)
        except ResponseException as e:
            raise e

        response_data = response[self.Response.KEY_DATA]

        return self.__class__(response_data, path_params=self.path_params)

    def id(self: 'BaseServiceCollectionApi', value: int) -> 'BaseServiceRecordApi':
        """
            collection内から該当するidのrecordを返します
        """
        if self.records is not None:
            target = self.records.get(str(value))
            if isinstance(target, BaseServiceRecordApi):
                target.path_params[self.RECORD_NAME] = str(value)
                return target
        raise Exception("存在しないIDです")


Unit = TypeVar('Unit', bound='BaseServiceRecordApi')

class BaseServiceRecordApi(BaseEntity, BaseServiceApi):
    RECORD_NAME: str


    def __init__(
        self,
        fetched_data: bool = False,
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        self.path_params: Dict[str, Union[str, None]] = copy.deepcopy(path_params)
        self.path_params[self.RECORD_NAME] = None

    def id(self: 'BaseServiceRecordApi', value: int) -> 'BaseServiceRecordApi':
        self.path_params[self.RECORD_NAME] = str(value)
        return self

    async def get(
        self: 'BaseServiceRecordApi',
        field: Optional[List] = None,
        **kwargs
    ) -> 'BaseServiceRecordApi':
        uri = self._get_uri(self.path_params)
        header = self._get_header()
        body = self._get_query(
            field=field,
            where_dict=kwargs
        )

        try:
            response = self._api_get(uri, header, body)
        except ResponseException as e:
            raise e

        response_data: Dict = response[self.Response.KEY_DATA]
        return self.__class__(
            data=response_data,
            fetched_data=True,
            path_params=self.path_params
        )

    @classmethod
    async def create(cls: Type[Unit], **kwargs) -> Unit:
        result = cls(kwargs)
        return result

    async def save(self: 'BaseServiceRecordApi', **kwargs) -> 'BaseServiceRecordApi':
        uri = self._get_uri([str(self._id)])
        header = self._get_header()
        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                setattr(self, k, v)
        self.__api_post(uri, header, self.to_api_request_body())
        return self

    async def update(self: 'BaseServiceRecordApi', **kwargs) -> 'BaseServiceRecordApi':
        uri = self._get_uri(self.path_params)

        header = self._get_header()
        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                setattr(self, k, v)
        self._api_patch(uri, header, self.to_api_request_body())
        return self

    async def delete(self: 'BaseServiceRecordApi', **kwargs) -> bool:
        return True

