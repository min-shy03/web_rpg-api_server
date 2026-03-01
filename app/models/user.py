from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # 로그인용 ID (12자 제한 유지)
    user_id = Column(String(12), unique=True, index=True, nullable=False)
    
    # 비밀번호 (암호화된 문자열 저장용)
    password = Column(String(255), nullable=False)
    
    # 닉네임 (8자 설계 반영)
    nickname = Column(String(8), unique=True, index=True, nullable=False)
    
    # 직업 아이디 (기본값 1: 전사 등)
    job_id = Column(Integer, nullable=False)

    # 생성 시간
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, nickname={self.nickname})>"