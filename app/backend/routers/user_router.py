from fastapi import APIRouter, Request, Response
from unidecode import unidecode

from app.backend.utils.user_validator import UserValidator

user_router = APIRouter()


@user_router.get(
    "/api/current_user",
    description="Retrieve username from cookie.",
)
def get_user(request: Request) -> str:
    """\f Retrieve username from the cookie - registration needed."""
    return request.cookies.get("X-Authorization")


@user_router.post(
    "/api/register",
    description="Set up username into cookie.",
)
def register_user(user: UserValidator, response: Response) -> None:
    """\f Set up cookie to username."""
    # Replace non ASCII chars in order to bug in starlette set_cookie hardcoded format as 'latin-1'.
    username: str = unidecode(user.username)
    response.set_cookie(
        key="X-Authorization", value=username, httponly=True
    )
