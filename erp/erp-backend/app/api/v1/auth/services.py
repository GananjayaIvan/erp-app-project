import httpx
from config import ZITADEL_DOMAIN, CLIENT_ID


async def exchange_code_for_token(code: str, code_verifier: str, redirect_uri: str):

    url = f"{ZITADEL_DOMAIN}/oauth/v2/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "code": code,
        "code_verifier": code_verifier,
        "redirect_uri": redirect_uri,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )

    if resp.status_code != 200:
        raise Exception(resp.text)

    return resp.json()