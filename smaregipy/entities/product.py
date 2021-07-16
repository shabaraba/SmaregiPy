from typing import Optional
import datetime
import dataclasses


@dataclasses.dataclass
class ProductEntity:
    product_id: Optional[int]
    category_id: Optional[int]
    product_code: Optional[str]
    product_name: Optional[str]
    product_kana: Optional[str]
    tax_division: Optional[int]
    product_price_division: Optional[int]
    price: Optional[int]
    customer_price: Optional[int]
    cost: Optional[int]
    attribute: Optional[str]
    description: Optional[str]
    catch_copy: Optional[str]
    size: Optional[str]
    color: Optional[str]
    tag: Optional[str]
    group_code: Optional[str]
    url: Optional[str]
    print_receipt_product_name: Optional[str]
    display_sequence: Optional[int]
    sales_division: Optional[int]
    stock_control_division: Optional[int]
    display_flag: Optional[bool]
    division: Optional[int]
    product_option_group_id: Optional[int]
    point_not_applicable: Optional[bool]
    tax_free_division: Optional[int]
    supplier_product_no: Optional[int]
    calc_discount: Optional[bool]
    staff_discount_rate: Optional[int]
    use_category_reduce_tax: Optional[int]
    reduce_tax_id: Optional[int]
    reduce_tax_price: Optional[int]
    reduce_tax_customer_price: Optional[int]
    app_start_date_time: Optional[datetime.datetime]
    ins_date_time: Optional[datetime.datetime]
    upd_date_time: Optional[datetime.datetime]


    def __init__(self, data: Optional[dict] = None):
        if isinstance(data, dict):
            self.product_id = data.get('productId')
            self.category_id = data.get('categoryId')
            self.product_code = data.get('productCode')
            self.product_name = data.get('productName')
            self.product_kana = data.get('productKana')
            self.tax_division = data.get('taxDivision')
            self.product_price_division = data.get('productPriceDivision')
            self.price = data.get('price')
            self.customer_price = data.get('customerPrice')
            self.cost = data.get('cost')
            self.attribute = data.get('attribute')
            self.description = data.get('description')
            self.catch_copy = data.get('catchCopy')
            self.size = data.get('size')
            self.color = data.get('color')
            self.tag = data.get('tag')
            self.group_code = data.get('groupCode')
            self.url = data.get('url')
            self.print_receipt_product_name = data.get('printReceiptProductName')
            self.display_sequence = data.get('displaySequence')
            self.sales_division = data.get('salesDivision')
            self.stock_control_division = data.get('stockControlDivision')
            self.display_flag = data.get('displayFlag')
            self.division = data.get('division')
            self.product_option_group_id = data.get('productOptionGroupId')
            self.point_not_applicable = data.get('pointNotApplicable')
            self.tax_free_division = data.get('taxFreeDivision')
            self.supplier_product_no = data.get('supplierProductNo')
            self.calc_discount = data.get('calcDiscount')
            self.staff_discount_rate = data.get('staffDiscountRate')
            self.use_category_reduce_tax = data.get('useCategoryReduceTax')
            self.reduce_tax_id = data.get('reduceTaxId')
            self.reduce_tax_price = data.get('reduceTaxPrice')
            self.reduce_tax_customer_price = data.get('reduceTaxCustomerPrice')
            self.app_start_date_time = data.get('appStartDateTime')
            self.ins_date_time = data.get('insDateTime')
            self.upd_date_time = data.get('updDateTime')

            self._id = self.product_id

    def to_api_request_body(self) -> dict:
        return {
            "categoryId": self.category_id,
            "productCode": self.product_code,
            "productName": self.product_name,
            "productKana": self.product_kana,
            "taxDivision": self.tax_division,
            "productPriceDivision": self.product_price_division,
            "price": self.price,
            "customerPrice": self.customer_price,
            "cost": self.cost,
            "attribute": self.attribute,
            "description": self.description,
            "catchCopy": self.catch_copy,
            "size": self.size,
            "color": self.color,
            "tag": self.tag,
            "groupCode": self.group_code,
            "url": self.url,
            "printReceiptProductName": self.print_receipt_product_name,
            "displaySequence": self.display_sequence,
            "salesDivision": self.sales_division,
            "stockControlDivision": self.stock_control_division,
            "displayFlag": self.display_flag,
            "division": self.division,
            "productOptionGroupId": self.product_option_group_id,
            "pointNotApplicable": self.point_not_applicable,
            "taxFreeDivision": self.tax_free_division,
            "supplierProductNo": self.supplier_product_no,
            "calcDiscount": self.calc_discount,
            "staffDiscountRate": self.staff_discount_rate,
            "useCategoryReduceTax": self.use_category_reduce_tax,
            "reduceTaxId": self.reduce_tax_id,
            "reduceTaxPrice": self.reduce_tax_price,
            "reduceTaxCustomerPrice": self.reduce_tax_customer_price,
            "appStartDateTime": self.app_start_date_time,
        }
