## database.py
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

# This used to create DB table
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
# )

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_ = AsyncSession,
    expire_on_commit=False,
)



class Base(DeclarativeBase):
    pass

# This provides database session
# def get_db():
#     with SessionLocal() as db:
#         yield db

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
