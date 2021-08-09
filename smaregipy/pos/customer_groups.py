import datetime
from pydantic import Field
from typing import (
    ClassVar,
    List,
    Dict,
    Optional,
)
from smaregipy.base_api import (
    BaseServiceRecordApi,
    BaseServiceCollectionApi,
)

from smaregipy.utils import NoData, DictUtil


class CustomerGroup(BaseServiceRecordApi):
    RECORD_NAME = 'customer_groups'
    ID_PROPERTY_NAME: ClassVar[str] = 'customer_group_id'
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = ['customer_group_id']

    customer_group_id: Optional[int] = Field(default_factory=NoData)
    customer_group_section_id: Optional[int] = Field(default_factory=NoData)
    label: Optional[str] = Field(default_factory=NoData)
    display_flag: Optional[bool] = Field(default_factory=NoData)
    display_sequence: Optional[int] = Field(default_factory=NoData)
    ins_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    upd_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 


class CustomerGroupCollection(BaseServiceCollectionApi[CustomerGroup]):
    RECORD_NAME = 'customer_groups'
    COLLECT_MODEL = CustomerGroup
    WITH: ClassVar[List[str]] = []


class CustomerGroupSection(BaseServiceRecordApi):
    RECORD_NAME = 'customer_group_sections'
    ID_PROPERTY_NAME: ClassVar[str] = 'customer_group_section_id'
    REQUEST_EXCLUDE_KEY: ClassVar[List[str]] = ['customer_group_section_id']

    customer_group_section_id: Optional[int] = Field(default_factory=NoData)
    customer_group_section_label: Optional[str] = Field(default_factory=NoData)
    ins_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 
    upd_date_time: Optional[datetime.datetime] = Field(default_factory=NoData) 

    async def save(self: 'CustomerGroupSection') -> 'CustomerGroupSection':
        """
            客層セクションの更新を行います。
            put処理のため、saveメソッドをオーバーライド
        """
        uri = self._get_uri(self._path_params)
        header = self._get_header()

        response = self._api_put(uri, header, self.to_api_request_body())
        response_data: Dict = DictUtil.convert_key_to_snake(response[self.Response.KEY_DATA])

        response_model = self.__class__(**response_data)
        self.copy_all_fields(response_model)
        self.id(getattr(self, self.ID_PROPERTY_NAME))
        self._status=self.DataStatus.SAVED
        return self

class CustomerGroupSectionCollection(BaseServiceCollectionApi[CustomerGroupSection]):
    RECORD_NAME = 'customer_group_sections'
    COLLECT_MODEL = CustomerGroupSection
    WITH: ClassVar[List[str]] = []
