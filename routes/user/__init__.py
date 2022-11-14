from . import posts
from fastapi.routing import APIRouter
from utils import dependencies

router = APIRouter(prefix='/user')

router.include_router(posts.router)