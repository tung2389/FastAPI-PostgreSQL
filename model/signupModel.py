from typing import Optional
from pydantic import BaseModel

class SignupModel(BaseModel):
    email: str
    password: str