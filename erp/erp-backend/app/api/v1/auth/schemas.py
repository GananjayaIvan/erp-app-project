from pydantic import BaseModel


class AuthCallbackRequest(BaseModel):
    code: str
    code_verifier: str
    redirect_uri: str

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    user: dict | None = None