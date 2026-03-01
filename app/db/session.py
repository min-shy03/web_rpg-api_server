import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db() :
    # async 으로 비동기 처리 (여러 사용자가 동시에 db에 접근할 수 있도록)
    # with 으로 db 접근이 끝난 세션은 삭제함으로써 db 과부화 방지
    async with AsyncSessionLocal() as session :
        # 이 함수를 실행한 장소로 반환(대여의 개념, return과의 차이점.) 후, 코드가 실행이 끝날 때 까지 대기하다가 다시 이 함수 실행
        yield session
        # 커밋이 끝날 때 까지 cpu가 다른 코드 실행하게끔 함
        await session.commit()