from jose import jwt, JWTError
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import models

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/jwt-login/')

def create_access_token(data: dict, expires: timedelta = None):
    to_encode = data.copy()
    expiry = datetime.now() + (expires or timedelta(minutes=15))
    to_encode.update({'exp': expiry})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def get_token_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username = payload.get('sub')
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need to login first!')
    return username
