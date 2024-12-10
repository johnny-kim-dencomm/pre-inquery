from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Member(Base):
    """
    사용자 정보
    """
    __tablename__ = "cst_member"

    member_uid: str | Column = Column(String(36), name="member_uid", primary_key=True, unique=True)
    email: str | Column = Column(String(255), name="email", nullable=False)
    nick_nm: str | Column = Column(String(100), name="nick_nm", nullable=False)
    birth_dy: str | Column = Column(String(10), name="birth_dy", nullable=True)
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    created_at: DateTime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", nullable=True)


class SnsLogin(Base):
    """
    사용자 SNS  로그인 정보
    """
    __tablename__ = "cst_sns_login"

    member_uid: str | Column = Column(String(36), ForeignKey("cst_member.member_uid"), primary_key=True)
    provider: str | Column = Column(String(50), name="provider", nullable=False, primary_key=True)
    accs_key: str | Column = Column(String(255), name="accs_key", nullable=False)
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))


class PwdLogin(Base):
    """
    사용자 비밀번호 로그인 정보
    """
    __tablename__ = "cst_pwd_login"

    member_uid: str | Column = Column(String(36), ForeignKey("cst_member.member_uid"), primary_key=True)
    password: str | Column = Column(String(100), name="password", nullable=False)
    updated_at: datetime | Column = Column(DateTime, name="updated_at", nullable=False, default=datetime.now(UTC))



