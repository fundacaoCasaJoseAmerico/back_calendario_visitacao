from anyio import ConnectionFailed
from fastapi import APIRouter, HTTPException, Request

router_v1 = APIRouter()

@router_v1.get("/status")
async def get_status():
    return {"status": "API v1 is running"}

@router_v1.get("/db-check")
async def db_check(request: Request):
    try:
        obj_acesso_db = request.app.state.db_client

        obj_acesso_db.db.client.admin.command('ping')

        return {"status": "ok", "message": "Conexão com o banco de dados bem-sucedida"}

    except ConnectionFailed as e:
        raise HTTPException(
            status_code=500,
            detail=f"Falha na conexão com o banco de dados: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ocorreu um erro inesperado: {e}"
        )
