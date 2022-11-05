from fastapi import FastAPI
from .libs.logger import Logger
from .configurations.dbinit import database

from .controllers import userController

def create_app():
    app = FastAPI()
    app.state.api_logger = Logger("INFO", "startup")

    app.include_router(userController.router)

    @app.on_event("startup")
    async def startup():
        app.state.db = database
        await app.state.db.connect()
        app.state.api_logger.info('Database connection established')

    @app.on_event("shutdown")
    async def shutdown():
        await app.state.db.disconnect()
        app.state.api_logger.info('Database connection closed')
    
    return app

app = create_app()