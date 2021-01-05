from fastapi import Request, HTTPException
from database import db
import jwt
from dotenv import load_dotenv
import os

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

async def authenticate(req: Request):

    try:
        authorization = req.headers["Authorization"]
        # Authorization header has the form "Bearer jwtToken"
        jwtToken = authorization[7:]
        data = jwt.decode(
            jwtToken,
            JWT_SECRET,
            algorithms='HS256',
        )
        userEmail = data['email']

        cursor = db.cursor()
        cursor.execute(f""" SELECT * FROM user_table WHERE email = '{userEmail}' """)
        user = cursor.fetchone()

        if user is None:
            raise HTTPException(
                status_code = 401,
                detail = "Unauthorized request"
            )
        
        return True
    except:
        raise HTTPException(
            status_code = 401,
            detail = "Unauthorized request"
        )

