from datetime import datetime
from pydantic import BaseModel, Field


class CodeInput(BaseModel):
    grp_cd: str | None = Field(title="grp_cd", description="그룹 코드", default=None)
    code_cd: str | None = Field(title="code_cd", description="코드", default=None)
    code_nm: str | None = Field(title="code_nm", description="코드명", default=None)
    flag1: str | None = Field(title="flag1", description="플래그1", default=None)
    flag2: str | None = Field(title="flag2", description="플래그2", default=None)
    flag3: str | None = Field(title="flag3", description="플래그3", default=None)
    order_no: int | None = Field(title="order_no", description="정렬 순서", default=None)
    use_yn: str | None = Field(title="use_yn", description="사용 여부", default=None)

    class Config:
        from_attribute=True


class CodeOutput(CodeInput):
    created_at: datetime | None = Field(title="created_at", description="등록 일시", default=None)
    created_by: str | None = Field(title="created_by", description="등록자 아이디", default=None)
    updated_at: datetime | None = Field(title="updated_at", description="최종 수정 일시", default=None)
    updated_by: str | None = Field(title="updated_by", description="최종 수정자 아이디", default=None)

    class Config:
        from_attribute=True
