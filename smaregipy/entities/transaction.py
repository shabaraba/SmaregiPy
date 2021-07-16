import dataclasses
from typing import Any, Dict, List, Optional
import datetime

from .base_entity import BaseEntity

@dataclasses.dataclass
class HeadEntity(BaseEntity):
    transaction_head_id: Optional[int]
    transaction_date_time: Optional[datetime.datetime]
    transaction_head_division: Optional[int]
    cancel_division: Optional[int]
    unit_non_discountsubtotal: Optional[int]
    unit_discountsubtotal: Optional[int]
    unit_staff_discountsubtotal: Optional[int]
    unit_bargain_discountsubtotal: Optional[int]
    subtotal: Optional[int]
    subtotal_for_discount: Optional[int]
    subtotal_discount_price: Optional[int]
    subtotal_discount_rate: Optional[int]
    subtotal_discount_division: Optional[int]
    point_discount: Optional[int]
    coupon_discount: Optional[int]
    total: Optional[int]
    tax_include: Optional[int]
    tax_exclude: Optional[int]
    rounding_division: Optional[int]
    rounding_price: Optional[int]
    cash_total: Optional[int]
    credit_total: Optional[int]
    deposit: Optional[int]
    deposit_cash: Optional[int]
    deposit_credit: Optional[int]
    change: Optional[int]
    tip_cash: Optional[int]
    tip_credit: Optional[int]
    amount: Optional[int]
    return_amount: Optional[int]
    cost_total: Optional[int]
    sales_head_division: Optional[int]
    in_tax_sales_total: Optional[int]
    out_tax_sales_total: Optional[int]
    non_tax_sales_total: Optional[int]
    non_sales_target_total: Optional[int]
    non_sales_target_out_tax_total: Optional[int]
    non_sales_target_in_tax_total: Optional[int]
    non_sales_target_tax_free_total: Optional[int]
    non_sales_target_cost_total: Optional[int]
    non_sales_target_amount: Optional[int]
    non_sales_target_return_amount: Optional[int]
    new_point: Optional[int]
    spend_point: Optional[int]
    point: Optional[int]
    total_point: Optional[int]
    current_mile: Optional[int]
    earn_mile: Optional[int]
    total_mile: Optional[int]
    adjustment_mile: Optional[int]
    adjustment_mile_division: Optional[int]
    adjustment_mile_value: Optional[int]
    store_id: Optional[int]
    store_code: Optional[str]
    terminal_id: Optional[int]
    customer_id: Optional[int]
    customer_code: Optional[str]
    terminal_tran_id: Optional[int]
    terminal_tran_date_time: Optional[datetime.datetime]
    sum_division: Optional[int]
    adjustment_date_time: Optional[datetime.datetime]
    sum_date: Optional[datetime.datetime]
    customer_rank: Optional[int]
    customer_group_id: Optional[int]
    customer_group_id2: Optional[int]
    customer_group_id3: Optional[int]
    customer_group_id4: Optional[int]
    customer_group_id5: Optional[int]
    staff_id: Optional[int]
    staff_code: Optional[str]
    staff_name: Optional[str]
    credit_division: Optional[int]
    payment_count: Optional[int]
    slip_number: Optional[int]
    cancel_slip_number: Optional[int]
    auth_number: Optional[int]
    auth_date: Optional[datetime.datetime]
    card_company: Optional[str]
    denomination: Optional[str]
    memo: Optional[str]
    receipt_memo: Optional[str]
    carriage: Optional[int]
    commission: Optional[int]
    guest_numbers: Optional[int]
    guest_numbers_male: Optional[int]
    guest_numbers_female: Optional[int]
    guest_numbers_unknown: Optional[int]
    enter_date_time: Optional[datetime.datetime]
    tax_free_sales_division: Optional[int]
    net_tax_free_general_tax_include: Optional[int]
    net_tax_free_general_tax_exclude: Optional[int]
    net_tax_free_consumable_tax_include: Optional[int]
    net_tax_free_consumable_tax_exclude: Optional[int]
    tags: Optional[str]
    point_giving_division: Optional[int]
    point_giving_unit_price: Optional[int]
    point_giving_unit: Optional[int]
    point_spend_division: Optional[int]
    mileage_division: Optional[int]
    mileage_label: Optional[str]
    customer_pin_code: Optional[str]
    return_sales: Optional[int]
    dispose_division: Optional[int]
    dispose_server_transaction_head_id: Optional[int]
    cancel_date_time: Optional[datetime.datetime]
    sell_division: Optional[int]
    tax_rate: Optional[int]
    tax_rounding: Optional[int]
    discount_rounding_division: Optional[int]
    transaction_uuid: Optional[datetime.datetime]
    exchange_ticket_no: Optional[int]
    gift_receipt_valid_days: Optional[datetime.date]
    barcode: Optional[str]
    upd_date_time: Optional[datetime.datetime]

    details: Any

    def __init__(self, head: dict):
        self.transaction_head_id = head.get('transactionHeadId')
        self.transaction_date_time = head.get('transactionDateTime')
        self.transaction_head_division = head.get('transactionHeadDivision')
        self.cancel_division = head.get('cancelDivision')
        self.unit_non_discountsubtotal = head.get('unitNonDiscountsubtotal')
        self.unit_discountsubtotal = head.get('unitDiscountsubtotal')
        self.unit_staff_discountsubtotal = head.get(
            'unitStaffDiscountsubtotal'
        )
        self.unit_bargain_discountsubtotal = head.get(
            'unitBargainDiscountsubtotal'
        )
        self.subtotal = head.get('subtotal')
        self.subtotal_for_discount = head.get('subtotalForDiscount')
        self.subtotal_discount_price = head.get('subtotalDiscountPrice')
        self.subtotal_discount_rate = head.get('subtotalDiscountRate')
        self.subtotal_discount_division = head.get('subtotalDiscountDivision')
        self.point_discount = head.get('pointDiscount')
        self.coupon_discount = head.get('couponDiscount')
        self.total = head.get('total')
        self.tax_include = head.get('taxInclude')
        self.tax_exclude = head.get('taxExclude')
        self.rounding_division = head.get('roundingDivision')
        self.rounding_price = head.get('roundingPrice')
        self.cash_total = head.get('cashTotal')
        self.credit_total = head.get('creditTotal')
        self.deposit = head.get('deposit')
        self.deposit_cash = head.get('depositCash')
        self.deposit_credit = head.get('depositCredit')
        self.change = head.get('change')
        self.tip_cash = head.get('tipCash')
        self.tip_credit = head.get('tipCredit')
        self.amount = head.get('amount')
        self.return_amount = head.get('returnAmount')
        self.cost_total = head.get('costTotal')
        self.sales_head_division = head.get('salesHeadDivision')
        self.in_tax_sales_total = head.get('inTaxSalesTotal')
        self.out_tax_sales_total = head.get('outTaxSalesTotal')
        self.non_tax_sales_total = head.get('nonTaxSalesTotal')
        self.non_sales_target_total = head.get('nonSalesTargetTotal')
        self.non_sales_target_out_tax_total = head.get(
            'nonSalesTargetOutTaxTotal'
        )
        self.non_sales_target_in_tax_total = head.get(
            'nonSalesTargetInTaxTotal'
        )
        self.non_sales_target_tax_free_total = head.get(
            'nonSalesTargetTaxFreeTotal'
        )
        self.non_sales_target_cost_total = head.get('nonSalesTargetCostTotal')
        self.non_sales_target_amount = head.get('nonSalesTargetAmount')
        self.non_sales_target_return_amount = head.get(
            'nonSalesTargetReturnAmount'
        )
        self.new_point = head.get('newPoint')
        self.spend_point = head.get('spendPoint')
        self.point = head.get('point')
        self.total_point = head.get('totalPoint')
        self.current_mile = head.get('currentMile')
        self.earn_mile = head.get('earnMile')
        self.total_mile = head.get('totalMile')
        self.adjustment_mile = head.get('adjustmentMile')
        self.adjustment_mile_division = head.get('adjustmentMileDivision')
        self.adjustment_mile_value = head.get('adjustmentMileValue')
        self.store_id = head.get('storeId')
        self.store_code = head.get('storeCode')
        self.terminal_id = head.get('terminalId')
        self.customer_id = head.get('customerId')
        self.customer_code = head.get('customerCode')
        self.terminal_tran_id = head.get('terminalTranId')
        self.terminal_tran_date_time = head.get('terminalTranDateTime')
        self.sum_division = head.get('sumDivision')
        self.adjustment_date_time = head.get('adjustmentDateTime')
        self.sum_date = head.get('sumDate')
        self.customer_rank = head.get('customerRank')
        self.customer_group_id = head.get('customerGroupId')
        self.customer_group_id2 = head.get('customerGroupId2')
        self.customer_group_id3 = head.get('customerGroupId3')
        self.customer_group_id4 = head.get('customerGroupId4')
        self.customer_group_id5 = head.get('customerGroupId5')
        self.staff_id = head.get('staffId')
        self.staff_code = head.get('staffCode')
        self.staff_name = head.get('staffName')
        self.credit_division = head.get('creditDivision')
        self.payment_count = head.get('paymentCount')
        self.slip_number = head.get('slipNumber')
        self.cancel_slip_number = head.get('cancelSlipNumber')
        self.auth_number = head.get('authNumber')
        self.auth_date = head.get('authDate')
        self.card_company = head.get('cardCompany')
        self.denomination = head.get('denomination')
        self.memo = head.get('memo')
        self.receipt_memo = head.get('receiptMemo')
        self.carriage = head.get('carriage')
        self.commission = head.get('commission')
        self.guest_numbers = head.get('guestNumbers')
        self.guest_numbers_male = head.get('guestNumbersMale')
        self.guest_numbers_female = head.get('guestNumbersFemale')
        self.guest_numbers_unknown = head.get('guestNumbersUnknown')
        self.enter_date_time = head.get('enterDateTime')
        self.tax_free_sales_division = head.get('taxFreeSalesDivision')
        self.net_tax_free_general_tax_include = head.get(
            'netTaxFreeGeneralTaxInclude'
        )
        self.net_tax_free_general_tax_exclude = head.get(
            'netTaxFreeGeneralTaxExclude'
        )
        self.net_tax_free_consumable_tax_include = head.get(
            'netTaxFreeConsumableTaxInclude'
        )
        self.net_tax_free_consumable_tax_exclude = head.get(
            'netTaxFreeConsumableTaxExclude'
        )
        self.tags = head.get('tags')
        self.point_giving_division = head.get('pointGivingDivision')
        self.point_giving_unit_price = head.get('pointGivingUnitPrice')
        self.point_giving_unit = head.get('pointGivingUnit')
        self.point_spend_division = head.get('pointSpendDivision')
        self.mileage_division = head.get('mileageDivision')
        self.mileage_label = head.get('mileageLabel')
        self.customer_pin_code = head.get('customerPinCode')
        self.return_sales = head.get('returnSales')
        self.dispose_division = head.get('disposeDivision')
        self.dispose_server_transaction_head_id = head.get(
            'disposeServerTransactionHeadId'
        )
        self.cancel_date_time = head.get('cancelDateTime')
        self.sell_division = head.get('sellDivision')
        self.tax_rate = head.get('taxRate')
        self.tax_rounding = head.get('taxRounding')
        self.discount_rounding_division = head.get('discountRoundingDivision')
        self.transaction_uuid = head.get('transactionUuid')
        self.exchange_ticket_no = head.get('exchangeTicketNo')
        self.gift_receipt_valid_days = head.get('giftReceiptValidDays')
        self.barcode = head.get('barcode')
        self.upd_date_time = head.get('updDateTime')

        self._id = self.transaction_head_id

    def to_api_request_body(self) -> dict:
        return {
            "transactionDateTime": self.transaction_date_time,
            "transactionHeadDivision": self.transaction_head_division,
            "cancelDivision": self.cancel_division,
            "unitNonDiscountSum": self.unit_non_discountsubtotal,
            "unitDiscountsubtotal": self.unit_discountsubtotal,
            "staffDiscountsubtotal": self.unit_staff_discountsubtotal,
            "unitBargainDiscountsubtotal": self.unit_bargain_discountsubtotal,
            "subtotal": self.subtotal,
            "subtotalForDiscount": self.subtotal_for_discount,
            "subtotalDiscountPrice": self.subtotal_discount_price,
            "subtotalDiscountRate": self.subtotal_discount_rate,
            "subtotalDiscountDivision": self.subtotal_discount_division,
            "pointDiscount": self.point_discount,
            "couponDiscount": self.coupon_discount,
            "total": self.total,
            "taxInclude": self.tax_include,
            "taxExclude": self.tax_exclude,
            "roundingDivision": self.rounding_division,
            "roundingPrice": self.rounding_price,
            "cashTotal": self.cash_total,
            "creditTotal": self.credit_total,
            "deposit": self.deposit,
            "depositCash": self.deposit_cash,
            "depositCredit": self.deposit_credit,
            "change": self.change,
            "tipCash": self.tip_cash,
            "tipCredit": self.tip_credit,
            "amount": self.amount,
            "returnAmount": self.return_amount,
            "costTotal": self.cost_total,
            "salesHeadDivision": self.sales_head_division,
            "inTaxSalesTotal": self.in_tax_sales_total,
            "outTaxSalesTotal": self.out_tax_sales_total,
            "nonTaxSalesTotal": self.non_tax_sales_total,
            "nonSalesTargetTotal": self.non_sales_target_total,
            "nonSalesTargetOutTaxTotal": self.non_sales_target_out_tax_total,
            "nonSalesTargetInTaxTotal": self.non_sales_target_in_tax_total,
            "nonSalesTargetTaxFreeTotal": self.non_sales_target_tax_free_total,
            "nonSalesTargetCostTotal": self.non_sales_target_cost_total,
            "nonSalesTargetAmount": self.non_sales_target_amount,
            "nonSalesTargetReturnAmount": self.non_sales_target_return_amount,
            "newPoint": self.new_point,
            "spendPoint": self.spend_point,
            "point": self.point,
            "totalPoint": self.total_point,
            "currentMile": self.current_mile,
            "earnMile": self.earn_mile,
            "totalMile": self.total_mile,
            "adjustmentMile": self.adjustment_mile,
            "adjustmentMileDivision": self.adjustment_mile_division,
            "adjustmentMileValue": self.adjustment_mile_value,
            "storeId": self.store_id,
            "storeCode": self.store_code,
            "terminalId": self.terminal_id,
            "customerId": self.customer_id,
            "customerCode": self.customer_code,
            "terminalTranId": self.terminal_tran_id,
            "terminalTranDateTime": self.terminal_tran_date_time,
            "sumDivision": self.sum_division,
            "adjustmentDateTime": self.adjustment_date_time,
            "sumDate": self.sum_date,
            "customerRank": self.customer_rank,
            "customerGroupId": self.customer_group_id,
            "customerGroupId2": self.customer_group_id2,
            "customerGroupId3": self.customer_group_id3,
            "customerGroupId4": self.customer_group_id4,
            "customerGroupId5": self.customer_group_id5,
            "staffId": self.staff_id,
            "staffCode": self.staff_code,
            "staffName": self.staff_name,
            "creditDivision": self.credit_division,
            "paymentCount": self.payment_count,
            "slipNumber": self.slip_number,
            "cancelSlipNumber": self.cancel_slip_number,
            "authNumber": self.auth_number,
            "authDate": self.auth_date,
            "cardCompany": self.card_company,
            "denomination": self.denomination,
            "memo": self.memo,
            "receiptMemo": self.receipt_memo,
            "carriage": self.carriage,
            "commission": self.commission,
            "guestNumbers": self.guest_numbers,
            "guestNumbersMale": self.guest_numbers_male,
            "guestNumbersFemale": self.guest_numbers_female,
            "guestNumbersUnknown": self.guest_numbers_unknown,
            "enterDateTime": self.enter_date_time,
            "taxFreeSalesDivision": self.tax_free_sales_division,
            "netTaxFreeGeneralTaxInclude": self.net_tax_free_general_tax_include,
            "netTaxFreeGeneralTaxExclude": self.net_tax_free_general_tax_exclude,
            "netTaxFreeConsumableTaxInclude": self.net_tax_free_consumable_tax_include,
            "netTaxFreeConsumableTaxExclude": self.net_tax_free_consumable_tax_exclude,
            "tags": self.tags,
            "pointGivingDivision": self.point_giving_division,
            "pointGivingUnitPrice": self.point_giving_unit_price,
            "pointGivingUnit": self.point_giving_unit,
            "pointSpendDivision": self.point_spend_division,
            "mileageDivision": self.mileage_division,
            "mileageLabel": self.mileage_label,
            "customerPinCode": self.customer_pin_code,
            "returnSales": self.return_sales,
            "disposeDivision": self.dispose_division,
            "disposeServerTransactionHeadId": self.dispose_server_transaction_head_id,
            "cancelDateTime": self.cancel_date_time,
            "sellDivision": self.sell_division,
            "taxRate": self.tax_rate,
            "taxRounding": self.tax_rounding,
            "discountRoundingDivision": self.discount_rounding_division,
            "transactionUuid": self.transaction_uuid,
            "exchangeTicketNo": self.exchange_ticket_no,
            "giftReceiptValidDays": self.gift_receipt_valid_days,
            "barcode": self.barcode,
        }

@dataclasses.dataclass
class DetailEntity(BaseEntity):
    transaction_head_id: Optional[int]
    transaction_detail_id: Optional[int]
    parent_transaction_detail_id: Optional[int]
    transaction_detail_division: Optional[int]
    product_id: Optional[int]
    product_code: Optional[str]
    product_name: Optional[str]
    print_receipt_product_name: Optional[str]
    color: Optional[str]
    size: Optional[str]
    group_code: Optional[str]
    tax_division: Optional[int]
    price: Optional[int]
    sales_price: Optional[int]
    unit_discount_price: Optional[int]
    unit_discount_rate: Optional[int]
    unit_discount_division: Optional[int]
    cost: Optional[int]
    quantity: Optional[int]
    unit_non_discount_sum: Optional[int]
    unit_discount_sum: Optional[int]
    unit_discounted_sum: Optional[int]
    cost_sum: Optional[int]
    category_id: Optional[int]
    category_name: Optional[str]
    discrimination_no: Optional[int]
    sales_division: Optional[int]
    product_division: Optional[int]
    inventory_reservation_division: Optional[int]
    point_not_applicable: Optional[bool]
    calc_discount: Optional[int]
    tax_free_division: Optional[int]
    tax_free_commodity_price: Optional[int]
    tax_free: Optional[int]
    product_bundle_group_id: Optional[int]
    discount_price_proportional: Optional[int]
    discount_point_proportional: Optional[int]
    discount_coupon_proportional: Optional[int]
    tax_include_proportional: Optional[int]
    tax_exclude_proportional: Optional[int]
    product_bundle_proportional: Optional[int]
    staff_discount_proportional: Optional[int]
    bargain_discount_proportional: Optional[int]
    rounding_price_proportional: Optional[int]
    product_staff_discountRate: Optional[int]
    staff_rank: Optional[int]
    staff_rank_name: Optional[str]
    staff_discount_rate: Optional[int]
    staff_discount_division: Optional[int]
    apply_staff_discount_rate: Optional[int]
    apply_staff_discount_price: Optional[int]
    bargain_id: Optional[int]
    bargain_name: Optional[str]
    bargain_division: Optional[int]
    bargain_value: Optional[int]
    apply_bargain_value: Optional[int]
    apply_bargain_discount_price: Optional[int]
    tax_rate: Optional[int]
    standard_tax_rate: Optional[int]
    modified_tax_rate: Optional[int]
    reduce_tax_id: Optional[int]
    reduce_tax_name: Optional[str]
    reduce_tax_rate: Optional[int]
    reduce_tax_price: Optional[int]
    reduce_tax_member_price: Optional[int]

    def __init__(self, detail: dict):
        # dict.get()は存在しないキーの場合Noneを返す
        self.transaction_head_id = detail.get("transactionHeadId")

        self.transaction_detail_id = detail.get("transactionDetailId")
        self.parent_transaction_detail_id = detail.get(
            "parentTransactionDetailId"
        )
        self.transaction_detail_division = detail.get(
            "transactionDetailDivision"
        )
        self.product_id = detail.get("productId")
        self.product_code = detail.get("productCode")
        self.product_name = detail.get("productName")
        self.print_receipt_product_name = detail.get("printReceiptProductName")
        self.color = detail.get("color")
        self.size = detail.get("size")
        self.group_code = detail.get("groupCode")
        self.tax_division = detail.get("taxDivision")
        self.price = detail.get("price")
        self.sales_price = detail.get("salesPrice")
        self.unit_discount_price = detail.get("unitDiscountPrice")
        self.unit_discount_rate = detail.get("unitDiscountRate")
        self.unit_discount_division = detail.get("unitDiscountDivision")
        self.cost = detail.get("cost")
        self.quantity = detail.get("quantity")
        self.unit_non_discount_sum = detail.get("unitNonDiscountSum")
        self.unit_discount_sum = detail.get("unitDiscountSum")
        self.unit_discounted_sum = detail.get("unitDiscountedSum")
        self.cost_sum = detail.get("costSum")
        self.category_id = detail.get("categoryId")
        self.category_name = detail.get("categoryName")
        self.discrimination_no = detail.get("discriminationNo")
        self.sales_division = detail.get("salesDivision")
        self.product_division = detail.get("product")
        self.inventory_reservation_division = detail.get(
            "inventoryReservationDivision"
        )
        self.point_not_applicable = detail.get("pointNotApplicable")
        self.calc_discount = detail.get("calcDiscount")
        self.tax_free_division = detail.get("taxFreeDivision")
        self.tax_free_commodity_price = detail.get("taxFreeCommodityPrice")
        self.tax_free = detail.get("taxFree")
        self.product_bundle_group_id = detail.get("productBundleGroupId")
        self.discount_price_proportional = detail.get(
            "discountPriceProportional"
        )
        self.discount_point_proportional = detail.get(
            "discountPointProportional"
        )
        self.discount_coupon_proportional = detail.get(
            "discountCouponProportional"
        )
        self.tax_include_proportional = detail.get("taxIncludeProportional")
        self.tax_exclude_proportional = detail.get("taxExcludeProportional")
        self.product_bundle_proportional = detail.get(
            "productBundleProportional"
        )
        self.staff_discount_proportional = detail.get(
            "staffDiscountProportional"
        )
        self.bargain_discount_proportional = detail.get(
            "bargainDiscountProportional"
        )
        self.rounding_price_proportional = detail.get(
            "roundingPriceProportional"
        )
        self.product_staff_discountRate = detail.get("productStaffDiscountRate")
        self.staff_rank = detail.get("staffRank")
        self.staff_rank_name = detail.get("staffRankName")
        self.staff_discount_rate = detail.get("staffDiscountRate")
        self.staff_discount_division = detail.get("staffDiscountDivision")
        self.apply_staff_discount_rate = detail.get("applyStaffDiscountRate")
        self.apply_staff_discount_price = detail.get("applyStaffDiscountPrice")
        self.bargain_id = detail.get("bargainId")
        self.bargain_name = detail.get("bargainName")
        self.bargain_division = detail.get("bargainDivision")
        self.bargain_value = detail.get("bargainValue")
        self.apply_bargain_value = detail.get("applyBargainValue")
        self.apply_bargain_discount_price = detail.get(
            "applyBargainDiscountPrice"
        )
        self.tax_rate = detail.get("taxRate")
        self.standard_tax_rate = detail.get("standardTaxRate")
        self.modified_tax_rate = detail.get("modifiedTaxRate")
        self.reduce_tax_id = detail.get("reduceTaxId")
        self.reduce_tax_name = detail.get("reduceTaxName")
        self.reduce_tax_rate = detail.get("reduceTaxRate")
        self.reduce_tax_price = detail.get("reduceTaxPrice")
        self.reduce_tax_member_price = detail.get("reduceTaxMemberPrice")

        self._id = self.transaction_detail_id

    def to_api_request_body(self) -> dict:
        return {
            "parentTransactionDetailId": self.parent_transaction_detail_id,
            "transactionDetailDivision": self.transaction_detail_division,
            "productId": self.product_id,
            "productCode": self.product_code,
            "productName": self.product_name,
            "printReceiptProductName": self.print_receipt_product_name,
            "color": self.color,
            "size": self.size,
            "groupCode": self.group_code,
            "taxDivision": self.tax_division,
            "price": self.price,
            "salesPrice": self.sales_price,
            "unitDiscountPrice": self.unit_discount_price,
            "unitDiscountRate": self.unit_discount_rate,
            "unitDiscountDivision": self.unit_discount_division,
            "cost": self.cost,
            "quantity": self.quantity,
            "unitNonDiscountSum": self.unit_non_discount_sum,
            "unitDiscountSum": self.unit_discount_sum,
            "unitDiscountedSum": self.unit_discounted_sum,
            "costSum": self.cost_sum,
            "categoryId": self.category_id,
            "categoryName": self.category_name,
            "discriminationNo": self.discrimination_no,
            "salesDivision": self.sales_division,
            "productPriceDivision": self.product_division,
            "inventoryReservationDivision": self.inventory_reservation_division,
            "pointNotApplicable": self.point_not_applicable,
            "calcDiscount": self.calc_discount,
            "taxFreeDivision": self.tax_free_division,
            "taxFreeCommodityPrice": self.tax_free_commodity_price,
            "taxFree": self.tax_free,
            "productBundleGroupId": self.product_bundle_group_id,
            "discountPriceProportional": self.discount_price_proportional,
            "discountPointProportional": self.discount_point_proportional,
            "discountCouponProportional": self.discount_coupon_proportional,
            "taxIncludeProportional": self.tax_include_proportional,
            "taxExcludeProportional": self.tax_exclude_proportional,
            "productBundleProportional": self.product_bundle_proportional,
            "staffDiscountProportional": self.staff_discount_proportional,
            "bargainDiscountProportional": self.bargain_discount_proportional,
            "roundingPriceProportional": self.rounding_price_proportional,
            "productStaffDiscountRate": self.product_staff_discountRate,
            "staffRank": self.staff_rank,
            "staffRankName": self.staff_rank_name,
            "staffDiscountRate": self.staff_discount_rate,
            "staffDiscountDivision": self.staff_discount_division,
            "applyStaffDiscountRate": self.apply_staff_discount_rate,
            "applyStaffDiscountPrice": self.apply_staff_discount_price,
            "bargainId": self.bargain_id,
            "bargainName": self.bargain_name,
            "bargainDivision": self.bargain_division,
            "bargainValue": self.bargain_value,
            "applyBargainValue": self.apply_bargain_value,
            "applyBargainDiscountPrice": self.apply_bargain_discount_price,
            "taxRate": self.tax_rate,
            "standardTaxRate": self.standard_tax_rate,
            "modifiedTaxRate": self.modified_tax_rate,
            "reduceTaxId": self.reduce_tax_id,
            "reduceTaxName": self.reduce_tax_name,
            "reduceTaxRate": self.reduce_tax_rate,
            "reduceTaxPrice": self.reduce_tax_price,
            "reduceTaxMemberPrice": self.reduce_tax_member_price,
        }
