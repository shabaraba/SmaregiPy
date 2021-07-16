from typing import List

class BaseEntity:
    path_params_id_list: List[int] = []

    def to_api_request_body(self) -> dict:
        return {}
