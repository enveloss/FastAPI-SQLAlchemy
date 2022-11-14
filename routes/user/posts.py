from modules import *
from fastapi.routing import APIRouter

router = APIRouter(prefix='/posts')

@router.get('/')
async def root():
    return {'posts': 'some list of posts'}