from fastapi_sqlalchemy import db
from src.models import model_customer
from src.schemas import schema_customer

def create_customer(param: schema_customer.Medmber):