from fastapi import FastAPI
from resources import auth


app = FastAPI()

app.include_router(auth.router)