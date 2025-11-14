from fastapi import APIRouter
from app.api.v1.routes_v1 import router_v1

api_router = APIRouter()

# Monta todas as rotas da v1 sob o prefixo /v1
api_router.include_router(router_v1, prefix="/v1")
