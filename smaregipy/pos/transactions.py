import copy
from pydantic import Field
import datetime
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
from smaregipy.base_api import (
    BaseServiceApi,
    BaseServiceRecordApi,
    BaseServiceCollectionApi
)
from smaregipy.utils import NoData

class TransactionDetail(BaseServiceRecordApi):
    RECORD_NAME = 'details'
    ID_PROPERTY_NAME: ClassVar[str] = 'transaction_detail_id'
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = [
        'transaction_head_id',
        'transaction_detail_id',
    ]

    transaction_head_id: Optional[int] = Field(default_factory=NoData)
    transaction_detail_id: Optional[int] = Field(default_factory=NoData)
    parent_transaction_detail_id: Optional[int] = Field(default_factory=NoData)
    transaction_detail_division: Optional[int] = Field(default_factory=NoData)
    product_id: Optional[int] = Field(default_factory=NoData)
    product_code: Optional[str] = Field(default_factory=NoData)
    product_name: Optional[str] = Field(default_factory=NoData)
    print_receipt_product_name: Optional[str] = Field(default_factory=NoData)
    color: Optional[str] = Field(default_factory=NoData)
    size: Optional[str] = Field(default_factory=NoData)
    group_code: Optional[str] = Field(default_factory=NoData)
    tax_division: Optional[int] = Field(default_factory=NoData)
    price: Optional[int] = Field(default_factory=NoData)
    sales_price: Optional[int] = Field(default_factory=NoData)
    unit_discount_price: Optional[int] = Field(default_factory=NoData)
    unit_discount_rate: Optional[float] = Field(default_factory=NoData)
    unit_discount_division: Optional[int] = Field(default_factory=NoData)
    cost: Optional[int] = Field(default_factory=NoData)
    quantity: Optional[int] = Field(default_factory=NoData)
    unit_non_discount_sum: Optional[int] = Field(default_factory=NoData)
    unit_discount_sum: Optional[int] = Field(default_factory=NoData)
    unit_discounted_sum: Optional[int] = Field(default_factory=NoData)
    cost_sum: Optional[int] = Field(default_factory=NoData)
    category_id: Optional[int] = Field(default_factory=NoData)
    category_name: Optional[str] = Field(default_factory=NoData)
    discrimination_no: Optional[int] = Field(default_factory=NoData)
    sales_division: Optional[int] = Field(default_factory=NoData)
    product_division: Optional[int] = Field(default_factory=NoData)
    inventory_reservation_division: Optional[int] = Field(default_factory=NoData)
    point_not_applicable: Optional[bool] = Field(default_factory=NoData)
    calc_discount: Optional[int] = Field(default_factory=NoData)
    tax_free_division: Optional[int] = Field(default_factory=NoData)
    tax_free_commodity_price: Optional[int] = Field(default_factory=NoData)
    tax_free: Optional[int] = Field(default_factory=NoData)
    product_bundle_group_id: Optional[int] = Field(default_factory=NoData)
    discount_price_proportional: Optional[int] = Field(default_factory=NoData)
    discount_point_proportional: Optional[int] = Field(default_factory=NoData)
    discount_coupon_proportional: Optional[int] = Field(default_factory=NoData)
    tax_include_proportional: Optional[int] = Field(default_factory=NoData)
    tax_exclude_proportional: Optional[int] = Field(default_factory=NoData)
    product_bundle_proportional: Optional[int] = Field(default_factory=NoData)
    staff_discount_proportional: Optional[int] = Field(default_factory=NoData)
    bargain_discount_proportional: Optional[int] = Field(default_factory=NoData)
    rounding_price_proportional: Optional[int] = Field(default_factory=NoData)
    product_staff_discountRate: Optional[int] = Field(default_factory=NoData)
    staff_rank: Optional[int] = Field(default_factory=NoData)
    staff_rank_name: Optional[str] = Field(default_factory=NoData)
    staff_discount_rate: Optional[int] = Field(default_factory=NoData)
    staff_discount_division: Optional[int] = Field(default_factory=NoData)
    apply_staff_discount_rate: Optional[int] = Field(default_factory=NoData)
    apply_staff_discount_price: Optional[int] = Field(default_factory=NoData)
    bargain_id: Optional[int] = Field(default_factory=NoData)
    bargain_name: Optional[str] = Field(default_factory=NoData)
    bargain_division: Optional[int] = Field(default_factory=NoData)
    bargain_value: Optional[int] = Field(default_factory=NoData)
    apply_bargain_value: Optional[int] = Field(default_factory=NoData)
    apply_bargain_discount_price: Optional[int] = Field(default_factory=NoData)
    tax_rate: Optional[int] = Field(default_factory=NoData)
    standard_tax_rate: Optional[int] = Field(default_factory=NoData)
    modified_tax_rate: Optional[int] = Field(default_factory=NoData)
    reduce_tax_id: Optional[int] = Field(default_factory=NoData)
    reduce_tax_name: Optional[str] = Field(default_factory=NoData)
    reduce_tax_rate: Optional[int] = Field(default_factory=NoData)
    reduce_tax_price: Optional[int] = Field(default_factory=NoData)
    reduce_tax_member_price: Optional[int] = Field(default_factory=NoData)


class TransactionDetailCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'details'
    COLLECT_MODEL = TransactionDetail

    WITH: ClassVar[List[str]] = []


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

        path_param_dict = {
            'transactions': None,
            'details': None,
            'out_file_async': None,
        }
        uri = self._get_uri(path_param_dict)
        header = self._get_header()
        where_dict = kwargs
        state = {
            'contractId': config.smaregi_config.contract_id,
            'field': field,
            'sort': sort,
            'where': copy.deepcopy(where_dict),
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

class Transaction(BaseServiceRecordApi):
    RECORD_NAME = 'transactions'

    transaction_head_id: Optional[int] = Field(default_factory=NoData)
    transaction_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    transaction_head_division: Optional[int] = Field(default_factory=NoData)
    cancel_division: Optional[int] = Field(default_factory=NoData)
    unit_non_discountsubtotal: Optional[int] = Field(default_factory=NoData)
    unit_discountsubtotal: Optional[int] = Field(default_factory=NoData)
    unit_staff_discountsubtotal: Optional[int] = Field(default_factory=NoData)
    unit_bargain_discountsubtotal: Optional[int] = Field(default_factory=NoData)
    subtotal: Optional[int] = Field(default_factory=NoData)
    subtotal_for_discount: Optional[int] = Field(default_factory=NoData)
    subtotal_discount_price: Optional[int] = Field(default_factory=NoData)
    subtotal_discount_rate: Optional[float] = Field(default_factory=NoData)
    subtotal_discount_division: Optional[int] = Field(default_factory=NoData)
    point_discount: Optional[int] = Field(default_factory=NoData)
    coupon_discount: Optional[int] = Field(default_factory=NoData)
    total: Optional[int] = Field(default_factory=NoData)
    tax_include: Optional[int] = Field(default_factory=NoData)
    tax_exclude: Optional[int] = Field(default_factory=NoData)
    rounding_division: Optional[int] = Field(default_factory=NoData)
    rounding_price: Optional[int] = Field(default_factory=NoData)
    cash_total: Optional[int] = Field(default_factory=NoData)
    credit_total: Optional[int] = Field(default_factory=NoData)
    deposit: Optional[int] = Field(default_factory=NoData)
    deposit_cash: Optional[int] = Field(default_factory=NoData)
    deposit_credit: Optional[int] = Field(default_factory=NoData)
    change: Optional[int] = Field(default_factory=NoData)
    tip_cash: Optional[int] = Field(default_factory=NoData)
    tip_credit: Optional[int] = Field(default_factory=NoData)
    amount: Optional[int] = Field(default_factory=NoData)
    return_amount: Optional[int] = Field(default_factory=NoData)
    cost_total: Optional[float] = Field(default_factory=NoData)
    sales_head_division: Optional[int] = Field(default_factory=NoData)
    in_tax_sales_total: Optional[int] = Field(default_factory=NoData)
    out_tax_sales_total: Optional[int] = Field(default_factory=NoData)
    non_tax_sales_total: Optional[int] = Field(default_factory=NoData)
    non_sales_target_total: Optional[int] = Field(default_factory=NoData)
    non_sales_target_out_tax_total: Optional[int] = Field(default_factory=NoData)
    non_sales_target_in_tax_total: Optional[int] = Field(default_factory=NoData)
    non_sales_target_tax_free_total: Optional[int] = Field(default_factory=NoData)
    non_sales_target_cost_total: Optional[float] = Field(default_factory=NoData)
    non_sales_target_amount: Optional[int] = Field(default_factory=NoData)
    non_sales_target_return_amount: Optional[int] = Field(default_factory=NoData)
    new_point: Optional[int] = Field(default_factory=NoData)
    spend_point: Optional[int] = Field(default_factory=NoData)
    point: Optional[int] = Field(default_factory=NoData)
    total_point: Optional[int] = Field(default_factory=NoData)
    current_mile: Optional[int] = Field(default_factory=NoData)
    earn_mile: Optional[int] = Field(default_factory=NoData)
    total_mile: Optional[int] = Field(default_factory=NoData)
    adjustment_mile: Optional[int] = Field(default_factory=NoData)
    adjustment_mile_division: Optional[int] = Field(default_factory=NoData)
    adjustment_mile_value: Optional[int] = Field(default_factory=NoData)
    store_id: Optional[int] = Field(default_factory=NoData)
    store_code: Optional[str] = Field(default_factory=NoData)
    terminal_id: Optional[int] = Field(default_factory=NoData)
    customer_id: Optional[int] = Field(default_factory=NoData)
    customer_code: Optional[str] = Field(default_factory=NoData)
    terminal_tran_id: Optional[int] = Field(default_factory=NoData)
    terminal_tran_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    sum_division: Optional[int] = Field(default_factory=NoData)
    adjustment_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    sum_date: Optional[datetime.date] = Field(default_factory=NoData)
    customer_rank: Optional[int] = Field(default_factory=NoData)
    customer_group_id: Optional[int] = Field(default_factory=NoData)
    customer_group_id2: Optional[int] = Field(default_factory=NoData)
    customer_group_id3: Optional[int] = Field(default_factory=NoData)
    customer_group_id4: Optional[int] = Field(default_factory=NoData)
    customer_group_id5: Optional[int] = Field(default_factory=NoData)
    staff_id: Optional[int] = Field(default_factory=NoData)
    staff_code: Optional[str] = Field(default_factory=NoData)
    staff_name: Optional[str] = Field(default_factory=NoData)
    credit_division: Optional[int] = Field(default_factory=NoData)
    payment_count: Optional[int] = Field(default_factory=NoData)
    slip_number: Optional[int] = Field(default_factory=NoData)
    cancel_slip_number: Optional[int] = Field(default_factory=NoData)
    auth_number: Optional[int] = Field(default_factory=NoData)
    auth_date: Optional[datetime.datetime] = Field(default_factory=NoData)
    card_company: Optional[str] = Field(default_factory=NoData)
    denomination: Optional[str] = Field(default_factory=NoData)
    memo: Optional[str] = Field(default_factory=NoData)
    receipt_memo: Optional[str] = Field(default_factory=NoData)
    carriage: Optional[int] = Field(default_factory=NoData)
    commission: Optional[int] = Field(default_factory=NoData)
    guest_numbers: Optional[int] = Field(default_factory=NoData)
    guest_numbers_male: Optional[int] = Field(default_factory=NoData)
    guest_numbers_female: Optional[int] = Field(default_factory=NoData)
    guest_numbers_unknown: Optional[int] = Field(default_factory=NoData)
    enter_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    tax_free_sales_division: Optional[int] = Field(default_factory=NoData)
    net_tax_free_general_tax_include: Optional[int] = Field(default_factory=NoData)
    net_tax_free_general_tax_exclude: Optional[int] = Field(default_factory=NoData)
    net_tax_free_consumable_tax_include: Optional[int] = Field(default_factory=NoData)
    net_tax_free_consumable_tax_exclude: Optional[int] = Field(default_factory=NoData)
    tags: Optional[str] = Field(default_factory=NoData)
    point_giving_division: Optional[int] = Field(default_factory=NoData)
    point_giving_unit_price: Optional[int] = Field(default_factory=NoData)
    point_giving_unit: Optional[float] = Field(default_factory=NoData)
    point_spend_division: Optional[int] = Field(default_factory=NoData)
    mileage_division: Optional[int] = Field(default_factory=NoData)
    mileage_label: Optional[str] = Field(default_factory=NoData)
    customer_pin_code: Optional[str] = Field(default_factory=NoData)
    return_sales: Optional[int] = Field(default_factory=NoData)
    dispose_division: Optional[int] = Field(default_factory=NoData)
    dispose_server_transaction_head_id: Optional[int] = Field(default_factory=NoData)
    cancel_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    sell_division: Optional[int] = Field(default_factory=NoData)
    tax_rate: Optional[float] = Field(default_factory=NoData)
    tax_rounding: Optional[int] = Field(default_factory=NoData)
    discount_rounding_division: Optional[int] = Field(default_factory=NoData)
    transaction_uuid: Optional[datetime.datetime] = Field(default_factory=NoData)
    exchange_ticket_no: Optional[int] = Field(default_factory=NoData)
    gift_receipt_valid_days: Optional[datetime.date] = Field(default_factory=NoData)
    barcode: Optional[str] = Field(default_factory=NoData)
    upd_date_time: Optional[datetime.datetime] = Field(default_factory=NoData)
    details: 'TransactionDetailCollection' = TransactionDetailCollection()


    @property
    def head(self):
        return self


class TransactionCollection(BaseServiceCollectionApi):
    RECORD_NAME = 'transactions'
    COLLECT_MODEL = Transaction
    WITH: ClassVar[List[str]] = ['details']


