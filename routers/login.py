from fastapi import APIRouter, HTTPException
import bcrypt
import jwt
from dotenv import load_dotenv
import os

from database import db
from model.loginModel import LoginModel

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

router = APIRouter()

@router.post('/', status_code = 200)
async def login(req: LoginModel):
    email = req.email
    password = req.password

    cursor = db.cursor()
    cursor.execute(f""" SELECT * FROM user_table WHERE email = '{email}' """)
    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code = 400,
            detail = "Email or password is incorrent!"
        )
    
    userEmail = user[0]
    userPassword = user[1]
    if bcrypt.checkpw(password.encode('utf-8'), userPassword.encode('utf-8')):
        jwtToken = jwt.encode(
            {'email': str(userEmail)}, 
            JWT_SECRET, 
            algorithm='HS256'
        ).decode('utf-8')

        return {
            'jwtToken': jwtToken, 
            'message': "Logged in successfully!"
        }
    
    else:
        raise HTTPException(
            status_code = 400,
            detail = "Email or password is incorrent!"
        )

