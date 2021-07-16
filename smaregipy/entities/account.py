import datetime
import pytz
from typing import Optional

class Account():
    def __init__(
        self: 'Account',
        contract_id: str,
        sub: Optional[str]=None,
        is_owner: Optional[bool]=False,
        access_token: Optional[str]=None,
        access_token_expiration_datetime: Optional[datetime.datetime]=None,
        user_access_token: Optional[str]=None
    ):
        self.contract_id = contract_id
        self.sub = sub
        self.is_owner = is_owner
        if access_token is not None and access_token_expiration_datetime is not None:
            self.access_token = Account.AccessToken(
                access_token,
                access_token_expiration_datetime
            )
        if user_access_token is not None:
            self.user_access_token = Account.UserAccessToken(user_access_token)


    class UserAccessToken():
        def __init__(self, _access_token):
            self._access_token = _access_token

        @property
        def access_token(self):
            return self._access_token


    class AccessToken():
        def __init__(self, _access_token: str, _expiration_datetime: datetime.datetime):
            self._access_token: str = _access_token
            self._expiration_datetime: datetime.datetime = _expiration_datetime

        @property
        def access_token(self) -> str:
            return self._access_token

        @access_token.setter
        def access_token(self, value):
            self._access_token = value

        @property
        def expiration_datetime(self) -> datetime.datetime:
            return self._expiration_datetime

        @expiration_datetime.setter
        def expiration_datetime(self, value):
            if type(value) == str:
                value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S %z')
            self._expiration_datetime = value

        def is_access_token_available(self):
            if self.access_token is None:
                return False
            if self.expiration_datetime is not None:
                now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
                if (self.expiration_datetime < now):
                    return False
            return True
