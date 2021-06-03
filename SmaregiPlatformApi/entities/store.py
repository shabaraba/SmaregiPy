import dataclasses


@dataclasses.dataclass
class Store:
    def __init__(self, data: dict):
        self.store_id = data.get('storeId')
        self.store_name = data.get('storeName')
        self.ins_date_time = data.get('insDateTime')
        self.upd_date_time = data.get('updDateTime')
