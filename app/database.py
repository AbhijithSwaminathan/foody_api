import aioredis
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)

# Redis connection
REDIS_URL = "redis://localhost:6379"
redis = aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)