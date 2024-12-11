from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base


class Code(Base):
    __tablename__ = "com_code"

    grp_cd: str | Column = Column(String(10), name="grp_cd", comment="그룹 코드", primary_key=True)
    code_cd: str | Column = Column(String(10), name="code_cd", comment="코드", primary_key=True)
    code_nm: str | Column = Column(String(50), name="code_nm", comment="코드명", nullable=False)
    flag1: str | Column = Column(String(30), name="flag1", comment="임시값1", nullable=True)
    flag2: str | Column = Column(String(30), name="flag2", comment="임시값2", nullable=True)
    flag3: str | Column = Column(String(30), name="flag3", comment="임시값3", nullable=True)
    order_no: int | Column = Column(Integer, name="order_no", comment="정렬 순서", nullable=False, default=1)
    use_yn: str | Column = Column(String(1), name="use_yn", comment="사용 여부", nullable=False, default="Y")
    created_at: datetime | Column = Column(DateTime, name="created_at", comment="등록 일시", nullable=False, default=datetime.now(UTC))
    created_by: str | Column = Column(String(50), name="created_by", comment="등록자 아이디", nullable=False)
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", comment="최종 수정 일시", nullable=False)
    updated_by: str | Column = Column(String(50), name="updated_by", comment="최종 수정자 아이디", nullable=False)