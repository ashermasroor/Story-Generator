from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .backend import router as SG_backend_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SG_backend_router)
