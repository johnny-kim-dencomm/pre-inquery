from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Member(Base):
    __tablename__ = "cst_member"

    member_uid: str | Column = Column(String(35), name="member_uid", primary_key=True, unique=True)
    email: str | Column = Column(String(255), name="email", nullable=False)
    nick_nm: str | Column = Column(String(100), name="nick_nm", nullable=False)
    birth_dy: str | Column = Column(String(10), name="birth_dy", nullable=True)
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    created_at: DateTime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", nullable=True)


class SnsLogin(Base):
    __tablename__ = "cst_sns_login"

    member_uid: str | Column = Column(String(35), ForeignKey("cst_member.member_uid"), primary_key=True)
    provider: str | Column = Column(String(50), name="provider", nullable=False, primary_key=True)
    accs_key: str | Column = Column(String(255), name="accs_key", nullable=False)
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    