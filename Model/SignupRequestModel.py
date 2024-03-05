from pydantic import BaseModel

class SignupRequestModel(BaseModel):
    username: str
    password: str
