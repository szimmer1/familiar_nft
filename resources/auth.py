from fastapi import Depends, APIRouter
import fastapi_login
import fastapi_login.exceptions

from models.api.auth import LoginRequest, LoginResponse, SignupRequest, SignupResponse

#TODO(shahar) real secret
manager = fastapi_login.LoginManager("secret", "/login")

router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
async def signup(request: SignupRequest) -> SignupResponse:
    user = get(account_id)
    if not user:
        user = create_or_exists(account_id, nonce)
    return SignupResponse(nonce=user.nonce)


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest = Depends()) -> LoginResponse:
    user = get_user(request.account_id)
    if not user:
        raise fastapi_login.exceptions.InvalidCredentialsException("user does not exist")
    if verify(request.account_id, request.signature, user.nonce):
        return LoginResponse(
            access_token=manager.create_access_token(data={"sub": request.account_id}),
        )
    raise fastapi_login.exceptions.InvalidCredentialsException("authentication failed")
