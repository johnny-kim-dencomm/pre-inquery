from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base


class Hospital(Base):
    __tablename__ = "hst_hospital"

    # 병원 UID
    hspt_uid: str | Column = Column(String(36), name="hspt_uid", primary_key=True, unique=True)
    # 병원명
    hspt_nm: str | Column = Column(String(100), name="hspt_nm", nullable=False)
    # 대표원장1 성명
    head1_nm: str | Column = Column(String(100), name="head1_nm", nullable=False)
    # 대표원장2 성명 (공동개원일 경우)
    head2_nm: str | Column = Column(String(100), name="head2_nm", nullable=True)
    # 대표원장3 성명 (공동개원일 경우)
    head3_nm: str | Column = Column(String(100), name="head3_nm", nullable=True)
    # 전화번호
    phone_no: str | Column = Column(String(20), name="phone_no", nullable=False)
    # 이메일
    email: str | Column = Column(String(255), name="email", nullable=True)
    # 진료 시작 시간
    work_begin: str | Column = Column(String(5), name="work_begin", nullable=False)
    # 진료 종료 시간
    work_end: str | Column = Column(String(5), name="work_end", nullable=False)
    # 사용 여부
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    # 등록 일시
    created_at: DateTime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    # 등록자 아이디
    created_by: str | Column = Column(String(50), name="created_by", nullable=False)
    # 최종 수정 일시
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", nullable=False)
    # 최종 수정자 아이디
    updated_by: str | Column = Column(String(50), name="updated_by", nullable=False)


class Reservation(Base):
    """
    병원 예약 정보
    """
    __tablename__ = "hst_reservation"

    # 예약 UID
    rsrv_uid: str | Column = Column(String(36), name="rsv_uid", primary_key=True, unique=True)
    # 병원 UID
    hspt_uid: str | Column = Column(String(36), ForeignKey("hst_hospital.hspt_uid", ondelete="CASCADE"))
    # 환자 UID
    member_uid: str | Column = Column(String(36), ForeignKey("cst_member.member_uid", ondelete="CASCADE"))
    # 예약 일자
    rsrv_dy: str | Column = Column(String(10), name="rsrv_dy", nullable=False)
    # 예약 시간
    rstv_hm: str | Column = Column(String(5), name="rsrv_hm", nullable=False)
    # 예약 결과 (방문 / 노쇼 / 취소)
    status_cd: str | Column = Column(String(10), name="status_cd", nullable=False, default="010")
    # 등록일시
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False, default=datetime.now(UTC))
    # 등록자 아이디
    created_by: str | Column = Column(String(50), name="created_by", nullable=False)
    # 최종 수정 일시
    updated_at: DateTime | Column = Column(DateTime, name="updated_at", nullable=False)
    # 최종 수정자 아이디
    updated_by: str | Column = Column(String(50), name="updated_by", nullable=False)