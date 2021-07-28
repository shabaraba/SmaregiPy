import dataclasses
import datetime
import copy
from typing import (
    Any,
    ClassVar,
    TypeVar,
    Type,
    Dict,
    List,
    Optional,
    Union,
    cast
)
from smaregipy.exceptions import ResponseException
from smaregipy.base_api import BaseServiceRecordApi, BaseServiceCollectionApi
from smaregipy.bases.entity import BaseEntity

@dataclasses.dataclass
class Entity(BaseEntity):
    ID_PROPERTY_NAME: ClassVar[str] = 'product_id'

    product_id: int 
    category_id: int 
    product_code: str 
    product_name: str 
    product_kana: str 
    tax_division: int 
    product_price_division: int 
    price: int 
    customer_price: int 
    cost: int 
    attribute: str 
    description: str 
    catch_copy: str 
    size: str 
    color: str 
    tag: str 
    group_code: str 
    url: str 
    print_receipt_product_name: str 
    display_sequence: int 
    sales_division: int 
    stock_control_division: int 
    display_flag: bool 
    division: int 
    product_option_group_id: int 
    point_not_applicable: bool 
    tax_free_division: int 
    supplier_product_no: int 
    calc_discount: bool 
    staff_discount_rate: int 
    use_category_reduce_tax: int 
    reduce_tax_id: int 
    reduce_tax_price: int 
    reduce_tax_customer_price: int 
    app_start_date_time: datetime.datetime 
    ins_date_time: datetime.datetime 
    upd_date_time: datetime.datetime 


    def to_api_request_body(self) -> dict:
        return dataclasses.asdict(self)

class Product(BaseServiceRecordApi):
    RECORD_NAME = 'products'
    ENTITY = Entity


class ProductCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'products'
    COLLECT_MODEL = Product

