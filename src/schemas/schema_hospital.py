from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class HospitalInput(BaseModel):
    hspt_nm: str | None = Field(title="hspt_nm", description="병원명", default=None)
    head1_nm: str | None = Field(title="head1_nm", description="원장1 성명", default=None)
    head2_nm: str | None = Field(title="head2_nm", description="원장2 성명", default=None)
    head3_nm: str | None = Field(title="head3_nm", description="원장3 성명", default=None)
    phone_no: str | None = Field(title="phone_no", description="전화번호", default=None)
    email: EmailStr | None = Field(title="email", description="이메일", default=None)
    work_begin: str | None = Field(title="work_begin", description="진료 시작 시간", default=None)
    work_end: str | None = Field(title="work_end", description="진료 종료 시간", default=None)

    class Config:
        from_attribute=True


class HospitalOutput(HospitalInput):
    hspt_uid: str | None = Field(title="hspt_uid", description="병원 UID", default=None)
    use_yn: str | None = Field(title="use_yn", description="사용 여부", default=None)
    created_at: datetime | None = Field(title="created_at", description="생성일시", default=None)
    created_by: str | None = Field(title="created_by", description="등록자 아이디", default=None)
    updated_at: datetime | None = Field(title="updated_at", description="최종 수정일시", default=None)
    updated_by: str | None = Field(title="updated_by", description="최종 수정자 아이디", default=None)

    class Config:
        from_attribute=True


class HospitalInput(BaseModel):
    hspt_nm: str | None = Field(title="hspt_nm", description="병원명", default=None)
    head1_nm: str | None = Field(title="head1_nm", description="원장1 성명", default=None)
    head2_nm: str | None = Field(title="head2_nm", description="원장2 성명", default=None)
    head3_nm: str | None = Field(title="head3_nm", description="원장3 성명", default=None)
    phone_no: str | None = Field(title="phone_no", description="전화번호", default=None)
    email: EmailStr | None = Field(title="email", description="이메일", default=None)
    work_begin: str | None = Field(title="work_begin", description="진료 시작 시간", default=None)
    work_end: str | None = Field(title="work_end", description="진료 종료 시간", default=None)

    class Config:
        from_attribute=True


class HospitalUpdate(HospitalInput):
    hspt_uid: str | None = Field(title="hspt_uid", description="병원 UID", default=None)
    use_yn: str | None = Field(title="use_yn", description="사용 여부", default=None)

    class Config:
        from_attribute=True


class ReservationInput(BaseModel):
    hspt_uid: str | None = Field(title="hspt_uid", description="병원 UID", default=None)
    member_uid: str | None = Field(title="member_uid", description="환자 UID", default=None)
    rsrv_dy: str | None = Field(title="rsrv_dy", description="예약 일자", default=None)
    rstv_hm: str | None = Field(title="rstv_hm", description="예약 시간", default=None)

    class Config:
        from_attribute=True


class ReservationOutput(ReservationInput):
    rsrv_uid: str | None = Field(title="rsrv_uid", description="예약 UID", default=None)
    status_cd: str | None = Field(title="status_cd", description="예약 결과", default=None)
    created_at: datetime | None = Field(title="created_at", description="등록 일시", default=None)
    created_by: str | None = Field(title="created_by", description="등록자 아이디", default=None)
    updated_at: datetime | None = Field(title="updated_at", description="최종 수정 일시", default=None)
    updated_by: str  | None = Field(title="updated_by", description="최종 수정자 아이디", default=None)

    class Config:
        from_attribute=True