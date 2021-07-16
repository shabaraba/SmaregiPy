from typing import List

class BaseEntity:
    def to_api_request_body(self) -> dict:
        return {}
