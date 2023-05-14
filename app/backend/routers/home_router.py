from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/backend/templates")
home_router = APIRouter()


@home_router.get(
    "/",
    response_class=HTMLResponse,
    description="Chat start page",
)
async def home(request: Request) -> Jinja2Templates:
    """
    \f Chat startpage to get user nickname to be placed in a cookie.

    Args:
        request (Request): data to be used in templating.

    Returns:
        Jinja2Templates: rendered homepage template.
    """
    return templates.TemplateResponse("home.html", {"request": request})
