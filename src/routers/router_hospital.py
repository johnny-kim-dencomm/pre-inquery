from fastapi import APIRouter, status, Path
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.schemas import schema_hospital
from src.services import service_hospital

router = APIRouter(
    tags=["Hospital Info"]
)


@router.get(
    path="/list",
    summary="병원 목록",
    response_class=JSONResponse,
    response_model=list[schema_hospital.HospitalOutput]
)
async def get_hospital_list():
    return await service_hospital.get_hospital_list()


@router.post(
    path="/save",
    summary="병원 등록",
    response_model=schema_hospital.HospitalOutput
)
async def post_hospital_create(
        param: schema_hospital.HospitalInput
):
    try:
        retval: str = service_hospital.create_hospital(hospital=param, user_id="system")
        hospital:schema_hospital.HospitalOutput = service_hospital.get_hospital(hspt_uid=retval)
        return hospital
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.put(
    path="/save",
    summary="병원 정보 수정",
    response_model=schema_hospital.HospitalOutput
)
async def post_hospital_create(
        param: schema_hospital.HospitalUpdate
):
    try:
        retval: str = service_hospital.update_hospital(hospital=param, user_id="system")
        hospital:schema_hospital.HospitalOutput = service_hospital.get_hospital(hspt_uid=retval)
        return hospital
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.get(
    path="/view/{hspt_uid}",
    summary="병원 정보",
    response_class=JSONResponse,
    response_model=schema_hospital.HospitalOutput
)
async def get_hospital_view(
        hspt_uid: str = Path(title="hspt_uid", description="병원 UID")
):
    return service_hospital.get_hospital(hspt_uid=hspt_uid)