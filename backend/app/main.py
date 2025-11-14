from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from app.api.main_routes import api_router
from contextlib import asynccontextmanager
from app.database.mongo_db import MongoDAO

MONGO_URI = "mongodb://localhost:27017"

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_client = MongoClient(MONGO_URI)
    app.state.db_client = MongoDAO(mongo_client)
    yield

    if isinstance(app.state.db_client, MongoDAO):
        app.state.db_client.db.client.close()

app = FastAPI(
    title="Calendário de visitas - FCJA",
    description="API para o sistema de agendamento de visitas da FCJA.",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    # Permite o acesso do frontend local
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
        },
    )

# Inclui todas as rotas da API
app.include_router(api_router, prefix="/api")

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "ok"}
