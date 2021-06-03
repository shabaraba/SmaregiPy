import datetime
import pytz


class UserInfo():
    def __init__(self, json):
        self._sub = json['sub']
        self._contract_id = json['contract']['id']
        self._is_owner = json['contract']['is_owner']

    @property
    def contract_id(self):
        return self._contract_id


class UserAccessToken():
    def __init__(self, _access_token):
        self._access_token = _access_token

    @property
    def access_token(self):
        return self._access_token


class AccessToken():
    def __init__(self, _access_token, _expiration_datetime):
        self.access_token = _access_token
        self.expiration_datetime = _expiration_datetime

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @property
    def expiration_datetime(self):
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
