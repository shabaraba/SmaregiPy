import re
from typing import Dict, Any, Optional, ClassVar
import json
import datetime

class Singleton:
    _instance = None
    _initialized = False
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._initialized = True
        return cls._instance

    def __init__(self, *args, **kwargs):
        if self._instance is False:
            super().__init__(*args, **kwargs)


class NoDataType(Singleton):
    ...
    def __call__(self):
        return NoDataType()

NoData = NoDataType()

class StringUtil:
    @staticmethod
    def camel_to_snake(s: str) -> str:
        return re.sub("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r"_\1", s).lower()

    @staticmethod
    def snake_to_camel(s: str) -> str:
        return re.sub("_(.)", lambda x:x.group(1).upper(), s)

class DictUtil:
    @staticmethod
    def convert_key_to_snake(d: dict) -> dict:
        result = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = DictUtil.convert_key_to_snake(v)
            result[StringUtil.camel_to_snake(k)] = v

        return result

    @staticmethod
    def convert_key_to_camel(d: dict) -> dict:
        result = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = DictUtil.convert_key_to_camel(v)
            result[StringUtil.snake_to_camel(k)] = v

        return result

    @staticmethod
    def convert_value_to_str(d: Dict[str, Any]) -> Dict[str, str]:
        result = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = DictUtil.convert_value_to_str(v)
            if type(v) is bool:
                v = str(int(v))
            if type(v) is int:
                v = str(v)
            result[k] = v
        return result


def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))
