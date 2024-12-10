from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base


class Code(Base):
    __tablename__ = "com_code"
    # 그룹 코드
    grp_cd: str | Column = Column(String(10), name="grp_cd", primary_key=True)
    # 코드
    code_cd: str | Column = Column(String(10), name="code_cd", primary_key=True)
    # 코드명
    code_nm: str | Column = Column(String(50), name="code_nm", nullable=False)
    # 플래그1
    flag1: str | Column = Column(String(30), name="flag1", nullable=True)
    # 플래그2
    flag2: str | Column = Column(String(30), name="flag2", nullable=True)
    # 플래그3
    flag3: str | Column = Column(String(30), name="flag3", nullable=True)
    # 정렬 순서
    order_no: int | Column = Column(Integer, nullable=False, default=1)
    # 사용 여부
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    # 등록 일시
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    # 등록자 아이디
    created_by: str | Column = Column(String(50), name="created_by", nullable=False)
    # 최종 수정 일시
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", nullable=False)
    # 최종 수정자 아이디
    updated_by: str | Column = Column(String(50), name="updated_by", nullable=False)