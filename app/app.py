from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stacks


def create_app() -> FastAPI:
    app = FastAPI(title="Kata CACIB", docs_url="/swagger",
                  redoc_url="/api/redoc",
                  openapi_url="/api/openapi.json")

    app.include_router(stacks.router)

    # For local development
    origins = [
        "http://localhost:8000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Generic health route to sanity check the API
    @app.get("/health")
    async def health() -> str:
        return "ok"

    return app
