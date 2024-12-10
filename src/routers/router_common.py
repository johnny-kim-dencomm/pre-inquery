from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.schemas import schema_common
from src.services import service_common

router = APIRouter(
    tags=["공통 관리"]
)


@router.post(
    path="/code/save",
    summary="코드 등록",
    response_class=JSONResponse
)
async def post_common_code_save(param: schema_common.CodeInput):
    try:
        ret_val: bool = await service_common.create_code(code=param, user_id="system")
        if ret_val:
            return {"result": "success"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.put(
    path="/code/save",
    summary="코드 정보 수정",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK
)
async def put_common_code_save(param: schema_common.CodeInput):
    """
    ### 코드 정보 수정
    * :param CodeInput: 수정할 코드 정보
    * :return: success: 성공
    """
    try:
        ret_val: bool = await service_common.update_code(code=param, user_id="system")
        if ret_val:
            return {"result": "success"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.get(
    path="/codes",
    response_class=JSONResponse,
    response_model=list[schema_common.CodeOutput],
    summary="코드 목록 조회"
)
async def get_common_codes(
        grp_cd: str | None = Query(title="grp_cd", description="그룹 코드", default=None),
        code_nm: str | None = Query(title="code_nm", description="코드명", default=None)
):
    try:
        code_list = await service_common.get_code_list(grp_cd=grp_cd, code_nm=code_nm)
        return code_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.delete(
    path="/code/delete",
    summary="코드 삭제",
    response_class=JSONResponse,
)
def delete_common_code(
        grp_cd: str = Query(title="grp_cd", description="그룹 코드"),
        code_cd: str = Query(title="code_cd", description="코드")
):
    """
    ## 코드 삭제
    * :param grp_cd: 그룹코드
    * :param code_cd: 코드
    * :return: 성공 : success
    """
    try:
        ret_val: bool = service_common.delete_code(grp_cd=grp_cd, code_cd=code_cd, user_id="system")
        if ret_val:
            return {"result": "success"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))