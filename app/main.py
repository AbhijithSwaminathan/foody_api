from fastapi import FastAPI, Depends

from .database import database, engine, metadata, redis


app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()
    await redis.ping()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await redis.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}
