from fastapi import Header, HTTPException

async def check_x_token(x_token: str=Header(default=None)):
    if x_token != '12345x-token': raise HTTPException(400, detail='Not Auth')