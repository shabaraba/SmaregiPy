import dataclasses
from typing import List, Optional
import datetime

from .base_entity import BaseEntity

@dataclasses.dataclass
class StoreEntity(BaseEntity):
    store_id: Optional[int]
    store_name: Optional[str]
    ins_date_time: Optional[datetime.datetime]
    upd_date_time: Optional[datetime.datetime]

    def __init__(self, data: dict):
        self.store_id = data.get('storeId')
        self.store_name = data.get('storeName')
        self.ins_date_time = data.get('insDateTime')
        self.upd_date_time = data.get('updDateTime')

        self._id = self.store_id

    def to_api_request_body(self) -> dict:
        return {
            "storeName": self.store_name,
        }
