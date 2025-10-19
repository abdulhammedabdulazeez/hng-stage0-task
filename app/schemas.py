from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str
    stack: str


class GetMeResponse(BaseModel):
    status: str
    user: User
    timestamp: str
    fact: str
