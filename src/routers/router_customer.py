from fastapi import APIRouter, status, Path
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.schemas import schema_customer
from src.services import service_customer

router = APIRouter(
    tags=["Customer Info"]
)


@router.post(
    path="/create",
    summary="회원정보 등록",
    response_class=JSONResponse
)
def post_customer_create(
        param: schema_customer.MemberInput
):
    try:
        retval = service_customer.create_customer(param)
        return {"member_uid": retval}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.get(
    path="/list",
    summary="등록된 회원 목록",
    response_class=JSONResponse,
    response_model=list[schema_customer.MemberInfo]
)
async def get_customer_list():
    try:
        member_list = await service_customer.get_member_list()
        return member_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.get(
    path="/view/{member_uid}",
    summary="회원정보 조회",
    response_class=JSONResponse,
    response_model=schema_customer.MemberInfo
)
async def get_customer(
        member_uid: str = Path(title="member_uid", description="사용자 UID")
):
    try:
        member_info = await service_customer.get_member(member_uid=member_uid)
        return member_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))