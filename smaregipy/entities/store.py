import dataclasses
import datetime


@dataclasses.dataclass
class Store:
    # store_id: int
    # store_name: str
    # ins_date_time: datetime.datetime
    # upd_date_time: datetime.datetime

    def __init__(self, data: dict):
        self.store_id = data.get('storeId')
        self.store_name = data.get('storeName')
        self.ins_date_time = data.get('insDateTime')
        self.upd_date_time = data.get('updDateTime')

