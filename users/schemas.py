from pydantic import BaseModel

class CustomUserSchema(BaseModel):
    email: str
    password: str