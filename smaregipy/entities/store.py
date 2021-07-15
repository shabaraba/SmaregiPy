from typing import List, Optional
import dataclasses
import datetime


@dataclasses.dataclass
class StoreEntity:
    store_id: Optional[int]
    store_name: Optional[str]
    ins_date_time: Optional[datetime.datetime]
    upd_date_time: Optional[datetime.datetime]

    def __init__(self, data: dict):
        self.store_id = data.get('storeId')
        self.store_name = data.get('storeName')
        self.ins_date_time = data.get('insDateTime')
        self.upd_date_time = data.get('updDateTime')

@dataclasses.dataclass
class StoreCollectionEntity:
    records:List

    def __init__(self, data: List):
        self.records = [StoreEntity(each_data) for each_data in data]
