from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ...domain.services.auth_service import AuthService
from ...infrastructure.config.settings import JWT_SECRET
from ...infrastructure.adapters.jwt_adapter import JWTAdapter

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_auth_service() -> AuthService:
    jwt_adapter = JWTAdapter(JWT_SECRET)
    return AuthService(jwt_adapter=jwt_adapter)

@router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    user = auth_service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.generate_jwt(user)
    return {"access_token": access_token, "token_type": "bearer"}

