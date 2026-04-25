"""FastAPI entrypoint with secure defaults, health checks, and structured logging."""

import logging
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import get_settings

settings = get_settings()

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger("mengpt-service")

app = FastAPI(title=settings.app_name, version="0.1.0")


@app.middleware("http")
async def add_security_headers(request: Request, call_next: Any) -> JSONResponse:
    """Inject baseline security headers for API responses."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    """Liveness probe endpoint."""
    return {"status": "ok", "environment": settings.app_env}


@app.get("/")
async def root() -> dict[str, str]:
    """Default endpoint for quick smoke testing."""
    logger.info("Root endpoint called")
    return {"message": f"{settings.app_name} is running"}