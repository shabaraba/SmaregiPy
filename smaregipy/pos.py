import json
from typing import (
    TypeVar,
    Type,
    Dict,
    List,
    Optional,
    cast
)
from . import entities
from .exceptions import ResponseException
from .base_api import BaseServiceRecordApi, BaseServiceCollectionApi


# class TransactionsApi(BaseServiceRecordApi):
#     def get_transaction_head_list(
#         self,
#         field=None,
#         sort=None,
#         where_dict=None
#     ) -> List[TransactionHead]:
#         self.uri = smaregi_config.uri_pos + '/transactions'

#         header = self._get_header()
#         body = self._get_query(sort=sort, where_dict=where_dict)

#         response = self._api_get(self.uri, header, body)
#         if response[0] != 200:
#             raise Exception(response[1])
#         response_data = response[1]
#         result = [TransactionHead(data) for data in response_data]
#         return result

#     def get_transaction_detail(self,transaction_head_id, field=None, sort=None, where_dict=None) -> List['TransactionDetail']:
#         self.uri = smaregi_config.uri_pos + '/transactions/' + transaction_head_id + '/details'
        
#         header = self._get_header()
#         body = self._get_query(sort=sort, where_dict=where_dict)
        
#         response = self._api_get(self.uri, header, body)
#         if response[0] != 200:
#             raise Exception(response[1])
#         response_data = response[1]
#         result = [TransactionDetail(data) for data in response_data]
#         return result
        

#     def get_transaction(self,transaction_head_id, field=None, sort=None, where_dict=None) -> Dict[str, 'TransactionHead' or 'TransactionDetail']:
#         """取引取得APIを実施します

#         Returns:
#             dict: head, detailsをキーに持つdict型。各々の要素はTransactionHead、TransactionDetail型
#         """
#         self.uri = smaregi_config.uri_pos + '/transactions/' + transaction_head_id
        
#         header = self._get_header()
#         body = self._get_query_for_detail(sort=sort, where_dict=where_dict)
        
#         response = self._api_get(self.uri, header, body)
#         if response[0] != 200:
#             raise Exception(response[1])
#         response_data = response[1]
#         result = {}
#         result["head"] = TransactionHead(response_data)
#         if response_data.get("details") is not None:
#             result["details"] = [TransactionDetail(data) for data in response_data.get("details")]
#         return result
        
    
#     def create_transaction_detail_csv(self, field=None, sort=None, where_dict=None):
#         """取引明細CSV作成APIを実施します

#         Args:
#             field (dict, optional): [description]. Defaults to None.
#             sort (dict, optional): [description]. Defaults to None.
#             whereDict (dict, optional): [description]. Defaults to None.
#         """
#         self.uri = smaregi_config.uri_pos + '/transactions/details/out_file_async'
        
#         header = self._get_header()

#         body = self._get_query_for_detail(sort=sort, where_dict=where_dict, state={
#             'contractId': smaregi_config.contract_id,
#             'field': field,
#             'sort': sort,
#             'where': where_dict,
#         })
        
#         response = self._api_post(self.uri, header, body)
#         if response[0] != 200:
#             raise Exception(response[1])
#         responseData = response[1]
#         return responseData


class Store(entities.StoreEntity, BaseServiceRecordApi):
    PATH_PARAMS = ['stores']

class StoreCollection(BaseServiceCollectionApi):
    PATH_PARAMS = ['stores']

    records: Dict[str, Store]

    def __init__(self, data: List):
        self.records = { 
            each_data['storeId']: Store(each_data) 
            for each_data in data 
        }

class Product(entities.ProductEntity, BaseServiceRecordApi):
    PATH_PARAMS = ['products']

class ProductCollection(BaseServiceCollectionApi):
    PATH_PARAMS = ['products']

    records: Dict[str, Product]

    def __init__(self, data: List):
        self.records = { 
            each_data['productId']: Product(each_data)
            for each_data in data
        }

class Transaction(entities.transaction.HeadEntity, BaseServiceRecordApi):
    PATH_PARAMS = ['transactions']

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)
        if data.get('details') is not None:
            detail_list = cast(List, data.get('details'))
            self.details = TransactionDetailCollection(detail_list)

class TransactionDetail(entities.transaction.DetailEntity, BaseServiceRecordApi):
    PATH_PARAMS = ['transactions', 'details']

Collection = TypeVar('Collection', bound='BaseServiceCollectionApi')

class TransactionDetailCollection(BaseServiceCollectionApi):
    PATH_PARAMS = ['transactions', 'details']

    records: Dict[str, entities.transaction.DetailEntity]

    def __init__(self, data: List):
        self.records = { 
            each_data['transactionDetailId']: TransactionDetail(each_data)
            for each_data in data
        }

    @classmethod
    async def create_csv(
        cls:Type[Collection],
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

        uri = cls._get_uri({cls.UNIT_NAME: None})
        header = cls._get_header()
        body = cls._get_query(
            field=field,
            sort=sort,
            limit=limit,
            page=page,
            where_dict=kwargs
        )

        try:
            response = cls._api_get(uri, header, body)
        except ResponseException as e:
            raise e

        response_data = response[cls.Response.KEY_DATA]

        return cls(response_data, fetched_data=True)
#         self.uri = smaregi_config.uri_pos + '/transactions/details/out_file_async'
        
#         header = self._get_header()

#         body = self._get_query_for_detail(sort=sort, where_dict=where_dict, state={
#             'contractId': smaregi_config.contract_id,
#             'field': field,
#             'sort': sort,
#             'where': where_dict,
#         })
        
#         response = self._api_post(self.uri, header, body)
#         if response[0] != 200:
#             raise Exception(response[1])
#         responseData = response[1]
#         return responseData
