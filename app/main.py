from fastapi import FastAPI
from app.routers import email
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(email.email_router)