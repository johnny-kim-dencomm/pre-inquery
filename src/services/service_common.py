from datetime import datetime, UTC
from sqlalchemy import text
from fastapi_sqlalchemy import db

from src.models import model_common
from src.schemas import schema_common


async def get_code_list(grp_cd: str | None, code_nm: str | None):
    try:
        stmt = """
            SELECT A.*
            FROM
                com_code A
            WHERE
                A.use_yn = 'Y'
        """
        if grp_cd is not None:
            stmt += f"AND A.grp_cd = {grp_cd}"

        if code_nm is not None:
            stmt += f"AND A.code_nm LIKE '%{code_nm}%"

        ret_list = db.session.execute(text(stmt)).fetchall()
        converted_list = list[schema_common.CodeOutput]
        if len(ret_list) > 0:
            for item in ret_list:
                c_item = schema_common.CodeOutput()
                c_item.grp_cd = item.grp_cd
                c_item.code_cd = item.code_cd
                c_item.code_nm = item.code_nm
                c_item.use_yn = item.use_yn
                c_item.order_no = item.order_no
                c_item.created_by = item.created_by
                c_item.created_at = item.created_at
                c_item.updated_by = item.updated_by
                c_item.updated_at = item.updated_at

            return converted_list
        else:
            return []

    except Exception as e:
        raise e


async def create_code(code: schema_common.CodeInput, user_id: str) -> bool:
    try:
        new_code = model_common.Code()
        new_code.grp_cd = code.grp_cd
        new_code.code_cd = code.code_cd
        new_code.code_nm = code.code_nm
        new_code.flag1 = code.flag1
        new_code.flag2 = code.flag2
        new_code.flag3 = code.flag3
        new_code.order_no = code.order_no
        new_code.use_yn = "Y"
        new_code.created_at = datetime.now(UTC)
        new_code.created_by = user_id
        new_code.updated_at = datetime.now(UTC)
        new_code.updated_by = user_id
        db.session.add(new_code)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e