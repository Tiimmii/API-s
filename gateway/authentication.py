import jwt
from django.conf import settings
from datetime import datetime, timedelta
import random
import string


def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class Get_token():    
    @staticmethod
    def get_access_token(payload):
        return jwt.encode(
            {"exp": datetime.now() + timedelta(minutes=5), **payload},
            settings.SECRET_KEY,
            algorithm="HS256"
        )
    
    @staticmethod
    def get_refresh_token():
        return jwt.encode(
            {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
            settings.SECRET_KEY,
            algorithm="HS256"
        )

class Authentication():
    @staticmethod
    def valid_token(token):
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        except Exception:
            return None
        
        exp = decoded_data["exp"]

        if datetime.now().timestamp() > exp:
            return None
        
        return decoded_data