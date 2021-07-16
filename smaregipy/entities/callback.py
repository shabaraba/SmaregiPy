import dataclasses
from typing import Optional

from .base_entity import BaseEntity

@dataclasses.dataclass
class CallbackEntity(BaseEntity):
    uuid: Optional[str]  # or request_code
    callback_url: Optional[str]
    state: Optional[str]

    def __init__(self, data: dict):
        self.uuid = data.get('uuid')
        self.callback_url = data.get('callback_url')
        self.state = data.get('state')


    def to_api_request_body(self) -> dict:
        return { }
