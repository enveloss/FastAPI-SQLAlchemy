from fastapi import FastAPI
from routes import user

# setuping fastapi
app = FastAPI()
app.include_router(user.router)

@app.get('/')
async def root():
    return {'msg': 'It is a template of fastapi'}