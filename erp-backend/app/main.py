from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="ERP System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include API routes
app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "ERP API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }