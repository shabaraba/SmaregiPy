import datetime
from pydantic import Field
from typing import (
    ClassVar,
    List,
    Optional,
)
from smaregipy.base_api import (
    BaseServiceRecordApi,
    BaseServiceCollectionApi,
)

from smaregipy.utils import NoData

class PointCondition(BaseServiceRecordApi):
    RECORD_NAME: ClassVar[str] = 'stores'
    ID_PROPERTY_NAME: ClassVar[str] = 'store_id'
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = [
        'store_id',
    ]

    store_id: Optional[int] = Field(default_factory=NoData)
    point_use_division: int = 0
    spend_rate: Optional[float] = Field(default_factory=NoData) 
    point_giving_unit_price: Optional[str] = Field(default_factory=NoData) 
    point_giving_unit: Optional[str] = Field(default_factory=NoData) 
    point_giving_division: Optional[int] = Field(default_factory=NoData) 
    point_use_unit: Optional[int] = Field(default_factory=NoData) 
    point_spend_division: Optional[int] = Field(default_factory=NoData) 
    point_spend_limit_division: Optional[int] = Field(default_factory=NoData) 
    expire_division: Optional[int] = Field(default_factory=NoData) 
    expire_limit: Optional[str] = Field(default_factory=NoData) 
    mileage_division: Optional[int] = Field(default_factory=NoData) 
    mileage_limit: Optional[int] = Field(default_factory=NoData) 


class ReceiptPrintInfo(BaseServiceRecordApi):
    RECORD_NAME: ClassVar[str] = 'stores'
    ID_PROPERTY_NAME: ClassVar[str] = 'store_id'

    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = [
        'store_id',
        'air_print_logo',
        'advertisement_image',
        'gift_receipt_image',
        'gift_receipt_note',
    ]

    store_id: Optional[int] = Field(default_factory=NoData) 
    header: Optional[str] = Field(default_factory=NoData) 
    footer: Optional[str] = Field(default_factory=NoData) 
    receipt_tax_office_stamp_comment: Optional[str] = Field(default_factory=NoData) 
    tax_office_name: Optional[str] = Field(default_factory=NoData) 
    air_print_logo: Optional[str] = Field(default_factory=NoData) 
    advertisement_image: Optional[str] = Field(default_factory=NoData) 
    gift_receipt_image: Optional[str] = Field(default_factory=NoData) 
    gift_receipt_note: Optional[str] = Field(default_factory=NoData) 
    discount_receipt_header: Optional[str] = Field(default_factory=NoData) 
    discount_receipt_footer: Optional[str] = Field(default_factory=NoData) 


class Store(BaseServiceRecordApi):
    RECORD_NAME: ClassVar[str] = 'stores'
    ID_PROPERTY_NAME: ClassVar[str] = 'store_id'

    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = [
        'store_id',
        'pause_flag',
        'ins_date_time',
        'upd_date_time',
        'face_payment_use_division',
    ]

    WITH: ClassVar[List[str]] = ['point_condition','receipt_print_info']

    store_id: Optional[int] = Field(default_factory=NoData) 
    store_code: Optional[str] = Field(default_factory=NoData) 
    store_name: Optional[str] = Field(default_factory=NoData) 
    store_abbr: Optional[str] = Field(default_factory=NoData) 
    print_receipt_store_name: Optional[str] = Field(default_factory=NoData) 
    print_stock_receipt_store_name: Optional[str] = Field(default_factory=NoData) 
    division: Optional[int] = Field(default_factory=NoData) 
    post_code: Optional[str] = Field(default_factory=NoData) 
    address: Optional[str] = Field(default_factory=NoData) 
    phone_number: Optional[str] = Field(default_factory=NoData) 
    fax_number: Optional[str] = Field(default_factory=NoData) 
    mail_address: Optional[str] = Field(default_factory=NoData) 
    homepage: Optional[str] = Field(default_factory=NoData) 
    temp_tran_mail_address: Optional[str] = Field(default_factory=NoData) 
    price_change_flag: Optional[bool] = Field(default_factory=NoData) 
    sell_division: Optional[int] = Field(default_factory=NoData) 
    sum_proc_division: Optional[int] = Field(default_factory=NoData) 
    sum_date_change_time: Optional[str] = Field(default_factory=NoData) 
    sum_ref_column: Optional[str] = Field(default_factory=NoData) 
    point_not_applicable: Optional[bool] = Field(default_factory=NoData) 
    tax_free_division: Optional[int] = Field(default_factory=NoData) 
    max_bundle_product_count: Optional[int] = Field(default_factory=NoData) 
    max_discount_rate: Optional[int] = Field(default_factory=NoData) 
    carriage_display_flag: Optional[bool] = Field(default_factory=NoData) 
    terminal_adjustment_cash_flag: Optional[bool] = Field(default_factory=NoData) 
    terminal_check_cash_flag: Optional[bool] = Field(default_factory=NoData) 
    waiter_adjustment_division: Optional[int] = Field(default_factory=NoData) 
    saving_auto_division: Optional[int] = Field(default_factory=NoData) 
    saving_auto_price: Optional[int] = Field(default_factory=NoData) 
    cancel_setting_division: Optional[int] = Field(default_factory=NoData) 
    rounding_division: Optional[str] = Field(default_factory=NoData) 
    discount_rounding_division: Optional[str] = Field(default_factory=NoData) 
    card_company_select_division: Optional[int] = Field(default_factory=NoData) 
    gift_receipt_valid_days: Optional[str] = Field(default_factory=NoData) 
    tax_label_normal: Optional[str] = Field(default_factory=NoData) 
    tax_label_reduce: Optional[str] = Field(default_factory=NoData) 
    pause_flag: Optional[bool] = Field(default_factory=NoData) 
    display_sequence: Optional[str] = Field(default_factory=NoData) 
    ins_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    upd_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    face_payment_use_division: Optional[int] = Field(default_factory=NoData) 
    point_condition: PointCondition = PointCondition()
    receipt_print_info: ReceiptPrintInfo = ReceiptPrintInfo()


class StoreCollection(BaseServiceCollectionApi[Store]):
    RECORD_NAME = 'stores'
    COLLECT_MODEL = Store

    WITH: ClassVar[List[str]] = ['point_condition','receipt_print_info']


# Store.update_forward_refs()

