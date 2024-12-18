from uuid import uuid4
from datetime import datetime, UTC
from fastapi_sqlalchemy import db
from src.models import model_customer
from src.schemas import schema_customer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_customer(param: schema_customer.MemberInput)->str:
    """
    신규 사용자 등록
    :param param: 회원 정보
    :return:
    """
    try:
        newMember = model_customer.Member()
        newMember.member_uid = uuid4()
        newMember.nick_nm = param.nick_nm
        newMember.email = param.email
        newMember.language = param.language
        newMember.address=param.address
        newMember.created_at = datetime.now(UTC)
        newMember.updated_at = datetime.now(UTC)
        newMember.use_yn = "Y"
        newMember.birth_dy = param.birth_dy

        db.session.add(newMember)
        db.session.commit()

        return str(newMember.member_uid)
    except Exception as e:
        db.session.rollback()
        raise  e


async def get_member_list():
    try:
        member_list = db.session.query(model_customer.Member).filter("Y" == model_customer.Member.use_yn).all()
        return member_list
    except Exception as e:
        raise e


async def get_member(member_uid: str):
    try:
        member = db.session.query(model_customer.Member).filter(member_uid == model_customer.Member.member_uid).first()
        return member
    except Exception as e:
        raise e


async def create_member_password(member_uid: str, password: str) -> bool:
    """
    사용자 비밀번호 등록

    Parameters
    ----------
    member_uid 회원 UID
    password 사용할 비밀번호

    Returns
    -------
    bool 성공여부
    """
    try:
        pwd = model_customer.PwdLogin()
        pwd.member_uid = member_uid
        pwd.password = pwd_context.hash(password)
        db.session.add(pwd)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e