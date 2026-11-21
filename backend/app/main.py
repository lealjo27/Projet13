import os
from fastapi import FastAPI

app = FastAPI(
    title=os.getenv("PROJECT_NAME", "FFE - Agent IA Ouvertures d'Échecs"),
    version="0.1.0",
)


@app.get("/api/v1/healthcheck", tags=["System"])
def healthcheck() -> dict[str, str]:
    """Vérifie que le conteneur FastAPI répond correctement."""
    return {
        "status": "ok",
        "service": "ffe-backend",
        "environment": os.getenv("APP_ENV", "unknown"),
    }
