from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html

from app.api.routes import router

app = FastAPI(
    redoc_url=None
)

app.include_router(router)


@app.get("/openapi.json", include_in_schema=False)
def openapi():
    return app.openapi()


@app.get("/redoc", include_in_schema=False)
def redoc():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="API Docs",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"
    )