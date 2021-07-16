import dataclasses
from typing import Optional

from .base_entity import BaseEntity

@dataclasses.dataclass
class CallbackEntity(BaseEntity):
    uuid: Optional[str]  # or request_code
    callback_uri: Optional[str]
    state: Optional[str]

    def __init__(self, data: dict):
        self.uuid = data.get('storeId')
        self.callback_uri = data.get('storeName')
        self.state = data.get('insDateTime')


    def to_api_request_body(self) -> dict:
        return { }
