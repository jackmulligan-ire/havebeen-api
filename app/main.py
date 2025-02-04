from fastapi import FastAPI
from routers import email

app = FastAPI()
app.include_router(email.email_router)