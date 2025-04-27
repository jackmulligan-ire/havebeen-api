from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import email

app = FastAPI()
app.include_router(email.email_router)

# CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://havebeen-client-1012251451645.europe-west1.run.app",
    "https://havebeen.xyz"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)