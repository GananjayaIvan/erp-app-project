from fastapi import APIRouter, HTTPException
from schemas import AuthCallbackRequest
from services import exchange_code_for_token

import jwt

router = APIRouter()


@router.post("/auth/callback")
async def auth_callback(payload: AuthCallbackRequest):

    try:
        token_data = await exchange_code_for_token(
            code=payload.code,
            code_verifier=payload.code_verifier,
            redirect_uri=payload.redirect_uri
        )

        access_token = token_data.get("access_token")
        refresh_token = token_data.get("refresh_token")

        # ⚠️ Optional: decode user info (no verification yet)
        user_info = None
        if access_token:
            user_info = jwt.decode(
                access_token,
                options={"verify_signature": False}
            )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user_info
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )