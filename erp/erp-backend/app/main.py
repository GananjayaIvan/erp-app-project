from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router


app = FastAPI(
    title="ERP Backend API",
    version="1.0.0",

    # Reverse proxy path
    root_path="/api",

    redoc_url=None,
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://erp.local",
        "http://localhost:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix="/v1"
)


@app.get("/redoc", include_in_schema=False)
def redoc():
    return get_redoc_html(
        openapi_url="/api/openapi.json",
        title="API Docs",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"
    )