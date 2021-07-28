import re

class StringUtil:

    @staticmethod
    def camel_to_snake(s: str) -> str:
        return re.sub("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r"_\1", s).lower()

class DictUtil:

    @staticmethod
    def convert_key_to_snake(d: dict) -> dict:
        result = {StringUtil.camel_to_snake(k): v for k, v in d.items()}

        return result

