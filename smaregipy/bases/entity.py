import dataclasses
import datetime
import copy
from typing import (
    ClassVar,
    List,
    Optional,
    TypeVar,
    Type,
)

from smaregipy.utils import StringUtil

T_BaseEntity = TypeVar('T_BaseEntity', bound='BaseEntity')

@dataclasses.dataclass
class BaseEntity:
    ID_PROPERTY_NAME: ClassVar[str] = 'id_name'

    id_: int = dataclasses.field(init=False, repr=True)
    
    def __post_init__(self):
        id_value = getattr(self, self.ID_PROPERTY_NAME)
        setattr(self, "id_", id_value)

    def to_api_request_body(self) -> dict:
        return {}
