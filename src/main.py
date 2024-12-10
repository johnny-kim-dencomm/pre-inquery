import logging
from contextlib import asynccontextmanager
from uvicorn import server
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from src.routers import router_customer, router_hospital
from src.models import model_customer
from src.database import engine
from src.const import const


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()


app = FastAPI(
    title="Dencomm Pre-Inquery mockup",
    description="덴컴 사전문진 목업 서비스",
    lifespan=lifespan,
)

# Midddleware 등록
app.add_middleware(middleware_class=DBSessionMiddleware, db_url=const.DB_URL)
# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def include_routers():
    # Include routers
    print("Include routers...")
    app.include_router(router=router_customer.router, prefix="/customer")
    app.include_router(router=router_hospital.router, prefix="/hospital")


def init_database():
    # Database Initializing
    print("Initializing database tables...")
    model_customer.Base.metadata.create_all(bind=engine)


@app.get("/")
def get_index(request: Request):
    return {"message": "Hello"}


async def startup():
    # Startup Event
    banner = f"""
        ██████╗ ███████╗███╗   ██╗ ██████╗ ██████╗ ███╗   ███╗███╗   ███╗                                                                                               
        ██╔══██╗██╔════╝████╗  ██║██╔════╝██╔═══██╗████╗ ████║████╗ ████║                                                                                               
        ██║  ██║█████╗  ██╔██╗ ██║██║     ██║   ██║██╔████╔██║██╔████╔██║                                                                                               
        ██║  ██║██╔══╝  ██║╚██╗██║██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║                                                                                               
        ██████╔╝███████╗██║ ╚████║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║                                                                                               
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝                                                                                               
        ██╗████████╗    ██████╗ ███████╗██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗     ██████╗ ███████╗███████╗██╗ ██████╗███████╗
        ██║╚══██╔══╝    ██╔══██╗██╔════╝██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝    ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝
        ██║   ██║       ██║  ██║█████╗  ██║   ██║█████╗  ██║     ██║   ██║██████╔╝██╔████╔██║█████╗  ██╔██╗ ██║   ██║       ██║   ██║█████╗  █████╗  ██║██║     █████╗  
        ██║   ██║       ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔═══╝ ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║       ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██╔══╝  
        ██║   ██║       ██████╔╝███████╗ ╚████╔╝ ███████╗███████╗╚██████╔╝██║     ██║ ╚═╝ ██║███████╗██║ ╚████║   ██║       ╚██████╔╝██║     ██║     ██║╚██████╗███████╗
        ╚═╝   ╚═╝       ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚══════╝
        """
    print(banner)
    print("Pre-inquery mockup api service start")

    # Include Router
    include_routers()
    # Initialize database
    init_database()


async def shutdown():
    goodbye_banner = f"""    
     ██████╗  ██████╗  ██████╗ ██████╗     ██████╗ ██╗   ██╗███████╗██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██║  ███╗██║   ██║██║   ██║██║  ██║    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██║   ██║██║   ██║██║   ██║██║  ██║    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ██████╔╝   ██║   ███████╗██╗
     ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚═════╝    ╚═╝   ╚══════╝╚═╝
                                       by DenComm IT Development Office
    """
    print(goodbye_banner)
    print("Pre-inquery mockup api service shutdown")


if __name__ == "__main__":
    server.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        loop="asyncio",
        reload=True,
        log_level=logging.INFO,
    )
