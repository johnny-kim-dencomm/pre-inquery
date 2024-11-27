from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class Medmber(BaseModel):
    member_uid: str | None = Field(title="member_uid", description="회원 UID", default=None)
    email: EmailStr | None = Field(title="email", description="회원 이메일", default=None)
    nick_nm: str | None = Field(title="nick_nm", description="회원 닉네임")
    birth_dy: str | None = Field(title="birth_dy", description="회원 생년월일")
    use_yn: str | None = Field(title="use_yn", description="회원 사용여부")
    created_at: datetime | None = Field(title="created_at", description="생성일시")
    updated_at: datetime | None = Field(title="updated_at", description="최종 수정일시")

    class Config:
        from_attributes = True