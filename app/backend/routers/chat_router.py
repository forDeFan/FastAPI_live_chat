from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/backend/templates")
chat_router = APIRouter()


@chat_router.get(
    "/chat",
    response_class=HTMLResponse,
    description="Chat room page",
)
async def chat(request: Request) -> Jinja2Templates:
    """
    \f Chat room page for messaging between multiple users.
    Takes user nickname/ usrename from registartion process cookie.

    Args:
        request (Request): to be used in templating.

    Returns:
        Jinja2Templates: rendered homepage template.
    """
    return templates.TemplateResponse("chat.html", {"request": request})
