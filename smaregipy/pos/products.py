from pydantic import Field
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
from smaregipy.base_api import BaseServiceRecordApi, BaseServiceCollectionApi
from smaregipy.utils import NoData


class Product(BaseServiceRecordApi):
    RECORD_NAME = 'products'
    ID_PROPERTY_NAME: ClassVar[str] = 'product_id'
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = [
        'product_id',
    ]

    product_id: Optional[int] = Field(defualt_factory=NoData) 
    category_id: Optional[int] = Field(default_factory=NoData) 
    product_code: Optional[str] = Field(default_factory=NoData) 
    product_name: Optional[str] = Field(default_factory=NoData) 
    product_kana: Optional[str] = Field(default_factory=NoData) 
    tax_division: Optional[int] = Field(default_factory=NoData) 
    product_price_division: Optional[int] = Field(default_factory=NoData) 
    price: Optional[int] = Field(default_factory=NoData) 
    customer_price: Optional[int] = Field(default_factory=NoData) 
    cost: Optional[float] = Field(default_factory=NoData) 
    attribute: Optional[str] = Field(default_factory=NoData) 
    description: Optional[str] = Field(default_factory=NoData) 
    catch_copy: Optional[str] = Field(default_factory=NoData) 
    size: Optional[str] = Field(default_factory=NoData) 
    color: Optional[str] = Field(default_factory=NoData) 
    tag: Optional[str] = Field(default_factory=NoData) 
    group_code: Optional[str] = Field(default_factory=NoData) 
    url: Optional[str] = Field(default_factory=NoData) 
    print_receipt_product_name: Optional[str] = Field(default_factory=NoData) 
    display_sequence: Optional[int] = Field(default_factory=NoData) 
    sales_division: Optional[int] = Field(default_factory=NoData) 
    stock_control_division: Optional[int] = Field(default_factory=NoData) 
    display_flag: Optional[bool] = Field(default_factory=NoData) 
    division: Optional[int] = Field(default_factory=NoData) 
    product_option_group_id: Optional[int] = Field(default_factory=NoData) 
    point_not_applicable: Optional[bool] = Field(default_factory=NoData) 
    tax_free_division: Optional[int] = Field(default_factory=NoData) 
    supplier_product_no: Optional[int] = Field(default_factory=NoData) 
    calc_discount: Optional[bool] = Field(default_factory=NoData) 
    staff_discount_rate: Optional[int] = Field(default_factory=NoData) 
    use_category_reduce_tax: Optional[int] = Field(default_factory=NoData) 
    reduce_tax_id: Optional[int] = Field(default_factory=NoData) 
    reduce_tax_price: Optional[int] = Field(default_factory=NoData) 
    reduce_tax_customer_price: Optional[int] = Field(default_factory=NoData) 
    app_start_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    ins_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    upd_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 


class ProductCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'products'
    COLLECT_MODEL = Product
    WITH: ClassVar[List[str]] = []


