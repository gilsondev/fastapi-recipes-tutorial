from fastapi import FastAPI, APIRouter

from app import __version__, __project__

app = FastAPI(title=__project__, openapi_url="/openapi.json")

router = APIRouter()


@router.get("/", status_code=200)
def root() -> dict:
    """Room GET"""
    return {"msg": "Recipes API", "version": __version__}


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
