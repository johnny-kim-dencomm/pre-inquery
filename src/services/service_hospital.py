from uuid import uuid4
from datetime import datetime, UTC
from fastapi_sqlalchemy import db
from src.models import model_hostpital
from src.schemas import schema_hospital


async def get_hospital_list():
    try:
        hospital_list: list[schema_hospital.HospitalOutput] = db.session.query(model_hostpital.Hospital).filter("Y" == model_hostpital.Hospital.use_yn).all()
        return hospital_list
    except Exception as e:
        raise e


def create_hospital(hospital: schema_hospital.HospitalInput, user_id: str) -> str:
    try:
        hspt = model_hostpital.Hospital()
        hspt.hspt_uid = uuid4()
        hspt.hspt_nm = hospital.hspt_nm
        hspt.email = hospital.email
        hspt.head1_nm = hospital.head1_nm
        hspt.head2_nm = hospital.head2_nm
        hspt.head3_nm = hospital.head3_nm
        hspt.phone_no = hospital.phone_no
        hspt.work_begin = hospital.work_begin
        hspt.work_end = hospital.work_end
        hspt.use_yn = "Y"
        hspt.created_at = datetime.now(UTC)
        hspt.updated_at = datetime.now(UTC)
        hspt.created_by = user_id
        hspt.updated_by = user_id

        db.session.add(hspt)
        db.session.flush()
        hspt_uid = hspt.hspt_uid
        db.session.commit()
        return hspt_uid
    except Exception as e:
        db.session.rollback()
        raise e


def get_hospital(hspt_uid: str) -> schema_hospital.HospitalOutput:
    try:
        hospital: schema_hospital.HospitalOutput = db.session.query(model_hostpital.Hospital).filter(model_hostpital.Hospital.hspt_uid == str(hspt_uid)).first()
        return hospital
    except Exception as e:
        raise e


def update_hospital(hospital: schema_hospital.HospitalUpdate, user_id: str) -> str:
    try:
        hspt = db.session.query(model_hostpital.Hospital).filter(model_hostpital.Hospital.hspt_uid == str(hospital.hspt_uid)).first()
        hspt.hspt_nm = hospital.hspt_nm
        hspt.email = hospital.email
        hspt.head1_nm = hospital.head1_nm
        hspt.head2_nm = hospital.head2_nm
        hspt.head3_nm = hospital.head3_nm
        hspt.phone_no = hospital.phone_no
        hspt.work_begin = hospital.work_begin
        hspt.work_end = hospital.work_end
        hspt.use_yn = hospital.use_yn
        hspt.updated_at = datetime.now(UTC)
        hspt.updated_by = user_id

        db.session.add(hspt)
        db.session.flush()
        hspt_uid = hspt.hspt_uid
        db.session.commit()
        return hspt_uid
    except Exception as e:
        db.session.rollback()
        raise e