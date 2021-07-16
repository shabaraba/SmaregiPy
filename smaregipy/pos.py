from typing import (
    Any,
    TypeVar,
    Type,
    Dict,
    List,
    Optional,
    Union,
    cast
)
from . import config
from . import entities
from .entities.base_entity import BaseEntity
from .exceptions import ResponseException
from .base_api import BaseServiceRecordApi, BaseServiceCollectionApi


class Store(entities.StoreEntity, BaseServiceRecordApi):
    RECORD_NAME = 'stores'

    def __init__(
        self,
        data: Dict[str, Any] = {},
        fetched_data: bool = False,
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceRecordApi.__init__(self, fetched_data, path_params)
        if fetched_data is True:
            entities.StoreEntity.__init__(self, data)
        

class StoreCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'stores'

    records: Dict[str, Store]

    def __init__(
        self,
        data: List = [],
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceCollectionApi.__init__(self, data, path_params)
        self.records = { 
            each_data['storeId']: Store(
                data=each_data,
                fetched_data=True,
                path_params=self.path_params,
            ) 
            for each_data in data
        }

class Product(entities.ProductEntity, BaseServiceRecordApi):
    RECORD_NAME = 'products'

    def __init__(
        self,
        data: Dict[str, Any] = {},
        fetched_data: bool = False,
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceRecordApi.__init__(self, fetched_data, path_params)
        if fetched_data is True:
            entities.ProductEntity.__init__(self, data)
        
class ProductCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'products'

    records: Dict[str, Product]

    def __init__(
        self,
        data: List = [],
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceCollectionApi.__init__(self, data, path_params)
        self.records = { 
            each_data['productId']: Product(
                data=each_data,
                fetched_data=True,
                path_params=self.path_params,
            )
            for each_data in data
        }

class Transaction(entities.transaction.HeadEntity, BaseServiceRecordApi):
    RECORD_NAME = 'transactions'

    def __init__(
        self,
        data: Dict[str, Any] = {},
        fetched_data: bool = False,
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceRecordApi.__init__(self, fetched_data, path_params)
        if fetched_data is True:
            entities.transaction.HeadEntity.__init__(self, data)
        if data.get('details') is not None:
            detail_list = cast(List, data.get('details'))
            self.details = TransactionDetailCollection(
                data=detail_list,
                path_params=self.path_params,
            )
        else:
            self.details = TransactionDetailCollection(
                path_params=self.path_params,
            )


class TransactionDetail(entities.transaction.DetailEntity, BaseServiceRecordApi):
    RECORD_NAME = 'details'

    def __init__(
        self,
        data: Dict[str, Any] = {},
        fetched_data: bool = False,
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        if fetched_data is True:
            entities.transaction.DetailEntity.__init__(self, data)
        BaseServiceRecordApi.__init__(self, fetched_data, path_params)

Collection = TypeVar('Collection', bound='BaseServiceCollectionApi')

class TransactionDetailCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'details'

    records: Dict[str, TransactionDetail]

    def __init__(
        self,
        data: List = [],
        path_params: Dict[str, Union[str, None]] = {},
        **kwargs
    ) -> None:
        BaseServiceCollectionApi.__init__(self, data, path_params)
        self.records = { 
            each_data['transactionDetailId']: TransactionDetail(
                data=each_data,
                fetched_data=True,
                path_params=self.path_params,
            )
            for each_data in data
        }

    async def create_csv(
        self: 'BaseServiceCollectionApi',
        field: Optional[List] = None,
        sort: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> entities.CallbackEntity:
        """取引明細CSV作成APIを実施します

        Args:
            field (dict, optional): [description]. Defaults to None.
            sort (dict, optional): [description]. Defaults to None.
            whereDict (dict, optional): [description]. Defaults to None.
        """

        path_param_dict = self.path_params
        path_param_dict['out_file_async'] = None
        uri = self._get_uri(path_param_dict)
        header = self._get_header()
        where_dict = kwargs
        state = {
            'contractId': config.smaregi_config.contract_id,
            'field': field,
            'sort': sort,
            # 'where': where_dict,
        }
        where_dict['state'] = state
        body = self._get_query(
            field=field,
            sort=sort,
            where_dict=where_dict
        )

        try:
            response = self._api_post(uri, header, body)
        except ResponseException as e:
            raise e

        response_data = response[self.Response.KEY_DATA]

        return entities.CallbackEntity({
            'uuid': response_data.get('requestCode'),
            'callback_url': response_data.get('callbackUrl'),
            'state': response_data.get('state')
        })
