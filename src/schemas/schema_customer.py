from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class MemberInput(BaseModel):
    email: EmailStr | None = Field(title="email", description="회원 이메일", default=None)
    nick_nm: str | None = Field(title="nick_nm", description="회원 닉네임", default=None)
    birth_dy: str | None = Field(title="birth_dy", description="회원 생년월일", default=None)
    language: str | None = Field(title="language", description="회원 사용 언어", default=None)
    address: str | None = Field(title="address", description="회원 주소", default=None)

    class Config:
        from_attributes = True


class MemberInfo(MemberInput):
    member_uid: str | None = Field(title="member_uid", description="회원 UID", default=None)
    use_yn: str | None = Field(title="use_yn", description="회원 사용여부")
    created_at: datetime | None = Field(title="created_at", description="생성일시")
    updated_at: datetime | None = Field(title="updated_at", description="최종 수정일시")

    class Config:
        from_attributes = True