import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_jwt_token(email: str):
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
