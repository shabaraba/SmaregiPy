from urllib.parse import urlencode
from typing import (
    Any,
    Dict,
    List
)
from SmaregiPlatformApi import smaregi_config
from SmaregiPlatformApi.entities.product import Product
from SmaregiPlatformApi.entities.store import Store
from SmaregiPlatformApi.entities.transaction import TransactionHead, TransactionDetail
from .base_api import BaseServiceApi


class TransactionsApi(BaseServiceApi):
    def get_transaction_head_list(
        self,
        field=None,
        sort=None,
        where_dict=None
    ) -> List[TransactionHead]:
        self.uri = smaregi_config.uri_pos + '/transactions'

        header = self._get_header()
        body = self._get_query(sort=sort, where_dict=where_dict)

        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise Exception(response[1])
        response_data = response[1]
        result = [TransactionHead(data) for data in response_data]
        return result

    def get_transaction_detail(self,transaction_head_id, field=None, sort=None, where_dict=None) -> List['TransactionDetail']:
        self.uri = smaregi_config.uri_pos + '/transactions/' + transaction_head_id + '/details'
        
        header = self._get_header()
        body = self._get_query(sort=sort, where_dict=where_dict)
        
        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise Exception(response[1])
        response_data = response[1]
        result = [TransactionDetail(data) for data in response_data]
        return result
        

    def get_transaction(self,transaction_head_id, field=None, sort=None, where_dict=None) -> Dict[str, 'TransactionHead' or 'TransactionDetail']:
        """取引取得APIを実施します

        Returns:
            dict: head, detailsをキーに持つdict型。各々の要素はTransactionHead、TransactionDetail型
        """
        self.uri = smaregi_config.uri_pos + '/transactions/' + transaction_head_id
        
        header = self._get_header()
        body = self._get_query_for_detail(sort=sort, where_dict=where_dict)
        
        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise Exception(response[1])
        response_data = response[1]
        result = {}
        result["head"] = TransactionHead(response_data)
        if response_data.get("details") is not None:
            result["details"] = [TransactionDetail(data) for data in response_data.get("details")]
        return result
        
    
    def create_transaction_detail_csv(self, field=None, sort=None, where_dict=None):
        """取引明細CSV作成APIを実施します

        Args:
            field (dict, optional): [description]. Defaults to None.
            sort (dict, optional): [description]. Defaults to None.
            whereDict (dict, optional): [description]. Defaults to None.
        """
        self.uri = smaregi_config.uri_pos + '/transactions/details/out_file_async'
        
        header = self._get_header()

        body = self._get_query_for_detail(sort=sort, where_dict=where_dict, state={
            'contractId': smaregi_config.contract_id,
            'field': field,
            'sort': sort,
            'where': where_dict,
        })
        
        response = self._api_post(self.uri, header, body)
        if response[0] != 200:
            raise Exception(response[1])
        responseData = response[1]
        return responseData


class ProductsApi(BaseServiceApi):
    def get_product_by_id(self, id: int, field = None, sort = None, where_dict:dict = None) -> 'Product':
        """商品取得APIを実施します

        Raises:
            Exception: 取得できなかった場合

        Returns:
            Product: [description]
        """
        self.uri = smaregi_config.uri_pos + '/products/' + str(id)

        header = self._get_header()
        body = self._get_query_for_detail('productId,productName', sort, where_dict)

        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise Exception(response[1])
        return Product(response[1])


class StoresApi(BaseServiceApi):
    def get_store_list(self, field=None, sort=None, where_dict=None) -> List['Store']:
        self.uri = smaregi_config.uri_pos + '/stores'

        header = self._get_header()
        body = self._get_query('storeId,storeName', sort, where_dict)

        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise response[1]
        response_data = response[1]

        return [Store(data) for data in response_data]

    def get_store_by_id(self, id, ield=None, sort=None, where_dict=None) -> 'Store':
        self.uri = smaregi_config.uri_pos + '/stores/' + id

        header = self._get_header()
        body = self._get_query_for_detail('storeId,storeName', sort, where_dict)

        response = self._api_get(self.uri, header, body)
        if response[0] != 200:
            raise response[1]
        response_data = response[1]

        return Store(response_data)
