from fastapi import FastAPI
from app.application.api.user_api import router as user_router
from app.application.api.auth_api import router as auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
