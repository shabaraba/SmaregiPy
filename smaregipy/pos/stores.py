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
from smaregipy import config
from smaregipy import entities
from smaregipy.exceptions import ResponseException
from smaregipy.base_api import BaseServiceRecordApi, BaseServiceCollectionApi
from smaregipy.bases.entity import BaseEntity

@dataclasses.dataclass
class Entity(BaseEntity):
    ID_PROPERTY_NAME: ClassVar[str] = 'store_id'

    store_id: int
    store_code: str
    store_name: str
    store_abbr: str
    print_receipt_store_name: str
    print_stock_receipt_store_name: str
    division: int
    post_code: str
    address: str
    phone_number: str
    fax_number: str
    mail_address: str
    homepage: str
    temp_tran_mail_address: str
    price_change_flag: bool
    sell_division: int
    sum_proc_division: int
    sum_date_change_time: str
    sum_ref_column: str
    point_not_applicable: bool
    tax_free_division: int
    max_bundle_product_count: int
    max_discount_rate: int
    carriage_display_flag: bool
    terminal_adjustment_cash_flag: bool
    terminal_check_cash_flag: bool
    waiter_adjustment_division: int
    saving_auto_division: int
    saving_auto_price: int
    cancel_setting_division: int
    rounding_division: int
    discount_rounding_division: int
    card_company_select_division: int
    gift_receipt_valid_days: str
    tax_label_normal: str
    tax_label_reduce: str
    pause_flag: bool
    display_sequence: str
    ins_date_time: datetime.datetime
    upd_date_time: datetime.datetime
    face_payment_use_division: Optional[int] = dataclasses.field(default=None)
    point_condition: Optional['PointCondition'] = dataclasses.field(default=None)
    receipt_print_info: Optional['ReceiptPrintInfo'] = dataclasses.field(default=None)


@dataclasses.dataclass
class PointCondition(BaseEntity):
    store_id: int
    point_use_division: int
    spend_rate: str
    point_giving_unit_price: str
    point_giving_unit: str
    point_giving_division: int
    point_use_unit: str
    point_spend_division: int
    point_spend_limit_division: int
    expire_division: int
    expire_limit: str
    mileage_division: int


@dataclasses.dataclass
class ReceiptPrintInfo(BaseEntity):
      store_id: int
      header: str
      footer: str
      receipt_tax_office_stamp_comment: str
      tax_office_name: str
      air_print_logo: str
      advertisement_image: str
      gift_receipt_image: str
      gift_receipt_note: str
      discount_receipt_header: str
      discount_receipt_footer: str


class Store(BaseServiceRecordApi):
    RECORD_NAME = 'stores'
    ENTITY = Entity


class StoreCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'stores'
    COLLECT_MODEL = Store

