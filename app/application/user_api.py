from fastapi import FastAPI, HTTPException
from ...domain.services.user_service import UserService
from ...domain.models.user import User

app = FastAPI()

user_service = UserService(...)

@app.post("/api/v1/users")
def register_user(user_data: User):
    try:
        user = user_service.register_user(user_data.dict())
        return {"message": "El usuario ha sido registrado exitosamente. Por favor verifique su email"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

