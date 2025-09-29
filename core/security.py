from datetime import datetime, timedelta
from authlib.jose import jwt, JoseError
from core.config import settings
import bcrypt

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Generate JWT token using Authlib with expiry claim.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    header = {"alg": ALGORITHM}
    token = jwt.encode(header, to_encode, SECRET_KEY)
    return token.decode('utf-8') if isinstance(token, bytes) else token  # Authlib returns bytes

def verify_token(token: str):
    """
    Verify JWT token and return claims if valid, else None.
    """
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        return claims
    except JoseError as e:
        print("❌ JWT decode error:", e)
        return None

def hash_password(password: str) -> str:
    """
    Hash password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify plain password against hashed password.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
