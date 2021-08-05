import pydantic
import base64
import requests
import json
import copy
from urllib.parse import urlencode
from enum import Enum, auto

from typing import (
    Any,
    ClassVar,
    Dict,
    Generic,
    Tuple,
    Optional,
    List,
    TypeVar,
    Type,
    Union
)

from .exceptions import ResponseException
from . import config
from .entities import Account
from smaregipy.utils import DictUtil, json_serial, NoData


T_BaseService = TypeVar('T_BaseService', bound='BaseServiceApi')
T_InputEachData = Dict[str, Any]
T_Record = TypeVar('T_Record', bound='BaseServiceRecordApi')
T_Collection = TypeVar('T_Collection', bound='BaseServiceCollectionApi')


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


class BaseServiceApi(pydantic.BaseModel, BaseApi):
    class Config:
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True

    class DataStatus(Enum):
        NON_SAVED = 0
        FETCHED = auto()
        SAVED = auto()


    RECORD_NAME: ClassVar[str]
    ID_PROPERTY_NAME: ClassVar[str]

    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = []
    WITH: ClassVar[List[str]] = []

    _path_params: Dict[str, Union[str, None]] = {}
    _status: DataStatus = DataStatus.NON_SAVED

    @classmethod
    def create_with_path_params_and_status(
        cls: Type[T_BaseService],
        path_params={},
        status=DataStatus.NON_SAVED,
        **kwargs
    ) -> T_BaseService:
        """
            apiのレスポンス経由でのみ呼ばれる
            当クラスを、特定のプロテクテッドメンバに値を入れてインスタンス化する
        """
        instance = cls(**kwargs)
        if path_params.get(instance.RECORD_NAME) is None:
            path_params[instance.RECORD_NAME] = None
        instance._path_params = path_params
        instance._status = status
        return instance

    def _set_path_params(self, path_params: Dict[str, Union[str, None]]) -> None:
        self._path_params = copy.deepcopy(path_params)
        self._path_params[self.RECORD_NAME] = None

    def is_no_data(self) -> bool:
        has_data_fields = []
        for k, v in self.__fields__.items():
            if (
                not k in ('_path_params','_status') and
                v is not NoData
            ):
                has_data_fields.append(k)

        return True if has_data_fields == [] else False

    @classmethod
    def _get_uri(
        cls: Type[T_BaseService],
        path_params: Optional[Dict[str, Union[str, None]]] = None
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

    @classmethod
    def _get_with_query(
        cls: Type[T_BaseService]
    ) -> dict:
        return {f"with_{key}": 'all' for key in cls.WITH}

    @staticmethod
    def _get_header():
        if isinstance(config.smaregi_config.access_token, Account.AccessToken):
            auth = "Bearer " + config.smaregi_config.access_token.token
            return {
                'Authorization': auth,
                'Content-Type': 'application/json',
            }
        raise Exception('')

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
                'sort': (','.join(
                    "{params}:{ascending}"
                    .format(params=k, ascending=v)
                    for k, v in sort.items()
                ))
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

    def _api_post(self, uri: str, header: Dict, body: str) -> Tuple[int, Any]:
        """POSTのAPIを実施します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.post(uri, headers=header, data=body)
        result = response.json()
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )

        return (response.status_code, result)

    def _api_patch(self, uri: str, header: Dict, body: str) -> Tuple[int, Any]:
        """PATCHのAPIを実施します

        Args:
            uri (str): [description]
            header (dict): [description]
            body (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.patch(uri, headers=header, data=body)
        result = response.json()
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )

        return (response.status_code, result)

    def _api_delete(self, uri: str, header: Dict) -> Tuple[int, Any]:
        """DELETEのAPIを実施します

        Args:
            uri (str): [description]
            header (dict): [description]

        Returns:
            Tuple[int, Any]: status, response の tuple statusが200でなければ、responseはエラー内容
        """
        response = requests.delete(uri, headers=header)
        if response.status_code not in [
            BaseApi.Response.STATUS_SUCCESS,
            BaseApi.Response.STATUS_ACCEPTED,
        ]:
            raise ResponseException(
                response.json()
            )

        return (response.status_code, True)


class BaseServiceRecordApi(BaseServiceApi):
    # 自身のクエリストリングを指定
    RECORD_NAME: ClassVar[str] = ''
    # 自身のidを指定(store_id) など
    ID_PROPERTY_NAME: ClassVar[str] = 'id_name'
    # postなどで指定できないフィールドを指定
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = []

    def __init__(self, **data):
        super().__init__(**data)
        self._path_params = {self.RECORD_NAME: None}
        self._status = BaseServiceApi.DataStatus.NON_SAVED

    def to_api_request_body(self) -> str:
        """
            API更新登録用のリクエストボディのため、
            当モデルを辞書型の文字列に変換します
        """
        params = self._convert_members_to_request_body_dict()
        params = json.dumps(params, default=json_serial)
        return params

    def _convert_members_to_request_body_dict(self) -> Dict[str, str]:
        """
            API更新登録用のリクエストボディのため、
            当モデルを辞書型に変換します
            その際、予約後（children、id_など）は要素に含めません
            ネスト対応済み
        """

        params = self.dict()
        params = self._remove_nodata_keys(params)
        # params = self._remove_model_keys(params)
        params = self._remove_exclude_keys(params)
        params = DictUtil.convert_key_to_camel(params)
        params = DictUtil.convert_value_to_str(params)
        return params

    def _remove_nodata_keys(self, d: Dict) -> Dict:
        result = {}
        for k, v in d.items():
            if v is not NoData:
                if isinstance(v, dict):
                    v = self._remove_nodata_keys(v)
                result[k] = v

        return result

    def _remove_exclude_keys(self, d: Dict) -> Dict:
        result = {}
        for k, v in d.items():
            if k not in self.REQUEST_EXCLUDE_KEY:
                if isinstance(v, dict):
                    sub = getattr(self, k)
                    v = sub._remove_exclude_keys(v)
                result[k] = v

        return result

    # def _remove_model_keys(self, d: Dict) -> Dict:
    #     model_keys = [
    #         '_path_params',
    #         '_id',
    #         'with_',
    #         '_status',
    #     ]

    #     result = {}
    #     for k, v in d.items():
    #         if k not in model_keys:
    #             if isinstance(v, dict):
    #                 v = self._remove_model_keys(v)
    #             result[k] = v

    #     return result


    def id(self: T_Record, value: int) -> T_Record:
        """
            対象のレコードを返します
        """
        if isinstance(self._path_params, Dict):
            self._path_params[self.RECORD_NAME] = str(value)
        if self._path_params is None:
            self._path_params = {
                self.RECORD_NAME: str(value)
        }
        for child in self.__dict__.values():
            if isinstance(child, BaseServiceApi):
                child.id(value)

        return self

    async def get(
        self: T_Record,
        field: Optional[List] = None,
        **kwargs
    ) -> T_Record:
        uri = self._get_uri(self._path_params)
        header = self._get_header()
        with_dict = self._get_with_query()
        where_dict = dict(with_dict, **kwargs)
        body = self._get_query(
            field=field,
            where_dict=where_dict
        )

        try:
            response = self._api_get(uri, header, body)
        except ResponseException as e:
            raise e

        response_data: Dict = DictUtil.convert_key_to_snake(response[self.Response.KEY_DATA])
        return self.__class__.create_with_path_params_and_status(
            path_params=self._path_params,
            status=self.DataStatus.FETCHED,
            **response_data
        )

    @classmethod
    async def create(cls: Type[T_Record], **kwargs) -> T_Record:
        # TODO
        result = cls(**kwargs)
        return result

    async def save(self: T_Record) -> T_Record:
        uri = self._get_uri(self._path_params)
        header = self._get_header()

        if self._status == self.DataStatus.NON_SAVED:
            response = self._api_post(uri, header, self.to_api_request_body())
        else:
            response = self._api_patch(uri, header, self.to_api_request_body())

        response_data: Dict = DictUtil.convert_key_to_snake(response[self.Response.KEY_DATA])
        response_model = self.__class__.create_with_path_params_and_status(
            path_params=self._path_params,
            _status=self.DataStatus.SAVED,
            **response_data
        )
        self.copy_all_fields(response_model)
        self.id(getattr(self, self.ID_PROPERTY_NAME))
        self._status=self.DataStatus.SAVED
        return self

    def copy_all_fields(self: 'BaseServiceRecordApi', target: 'BaseServiceRecordApi') -> 'BaseServiceRecordApi':
        """
            APIで作成/更新した際にレスポンスで送られてくるデータを、
            現モデルのフィールドにコピーします
            （あらたにインスタンスを作成するとidが変わってしまうため行わない）
        """
        if self.__class__ is target.__class__:
            for k in target.__fields__:
                setattr(self, k, getattr(target, k))
        return self

    async def update(self: T_Record, **kwargs) -> T_Record:
        uri = self._get_uri(self._path_params)

        header = self._get_header()
        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                setattr(self, k, v)
        self._api_patch(uri, header, self.to_api_request_body())
        return self

    async def delete(self: 'BaseServiceRecordApi') -> bool:
        uri = self._get_uri(self._path_params)
        header = self._get_header()
        self._api_delete(uri, header)
        return True


class BaseServiceCollectionApi(BaseServiceApi, Generic[T_Record]):
    RECORD_NAME: ClassVar[str]
    COLLECT_MODEL: ClassVar[T_Record]

    records: List[T_Record] = []

    def __init__(self, **kwargs) -> None:
        # params = {
        #     'records': [kwargs]
        # }
        
        super().__init__(**kwargs)
        self._path_params = {self.RECORD_NAME: None}
        self._status = BaseServiceApi.DataStatus.NON_SAVED

    def __iter__(self):
        return iter(self.records)

    def __getitem__(self, item):
        return self.records[item]

    async def get_all(
        self: T_Collection,
        field: Optional[List] = None,
        sort: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> T_Collection:
        return await self.get_list(field, sort, **kwargs)

    async def get_list(
        self: T_Collection,
        field: Optional[List] = None,
        sort: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        **kwargs
    ) -> T_Collection:
        uri = self._get_uri(self._path_params)
        header = self._get_header()
        with_dict = self._get_with_query()
        where_dict = dict(with_dict, **kwargs)
        body = self._get_query(
            field=field,
            sort=sort,
            limit=limit,
            page=page,
            where_dict=where_dict
        )

        try:
            response = self._api_get(uri, header, body)
        except ResponseException as e:
            raise e

        response_data = response[self.Response.KEY_DATA]
        snake_case_converted = [DictUtil.convert_key_to_snake(data) for data in response_data]
        dict_For_pydantic = self._add_records_key(snake_case_converted)
        response_model_list = self._create_collect_model_instances(snake_case_converted)

        model: Type[T_Collection] = getattr(self, '__class__')
        return model.create_with_path_params_and_status(
            records=response_model_list,
            path_params=self._path_params,
            status=self.DataStatus.FETCHED,
        )

    def _add_records_key(self, data: List[T_InputEachData]) -> List[T_InputEachData]:
        #TODO できたらBaseServiceApiへ移動する
        ...


    def _create_collect_model_instances(self, data: List[T_InputEachData]) -> List[T_Record]:
        model: Type[T_Record] = getattr(self, 'COLLECT_MODEL')
        records = [
            model.create_with_path_params_and_status(
                path_params=self._path_params,
                status=self.DataStatus.FETCHED,
                **each_data
            ) for each_data in data
        ]

        return records

    def id(self: 'BaseServiceCollectionApi', value: int) -> T_Record:
        """
            collection内から該当するidのrecordを返します
        """
        if self.records is not None:
            id_key_dict: Dict[str, T_Record] = {
                str(getattr(record, record.ID_PROPERTY_NAME, None)): record
                for record in self.records
            }

            target = id_key_dict.get(str(value))
            if isinstance(target, BaseServiceRecordApi):
                target.id(value)
                return target
        raise Exception("存在しないIDです")

BaseServiceRecordApi.update_forward_refs()
BaseServiceCollectionApi.update_forward_refs()
