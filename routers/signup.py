from fastapi import APIRouter, HTTPException
import bcrypt
from database import db
from model.signupModel import SignupModel

router = APIRouter()

@router.post('/', status_code = 201)
async def signup(req: SignupModel):
    email = req.email
    password = req.password

    if not password:
        raise HTTPException(
            status_code = 400,
            detail = "Password cannot be emptied!"
        )
        
    cursor = db.cursor()
    cursor.execute(f""" SELECT * FROM user_table WHERE email = '{email}' """)
    user = cursor.fetchone()

    if user is None:
        hashPassword = bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute(f""" INSERT INTO user_table (email, password) VALUES ('{email}', '{hashPassword}') """)
        db.commit()
        return {'message': "Your account has been created!"}
    else:
        raise HTTPException(
            status_code = 400,
            detail = "The email has been used!"
        )


    

    
    
