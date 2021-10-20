from pydantic import BaseModel


class LoginRequest(BaseModel):
    account_id: str
    signature: str


class LoginResponse(BaseModel):
    token: str


class SignupRequest(BaseModel):
    account_id: str


class SignupResponse(BaseModel):
    nonce: str