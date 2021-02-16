from fastapi import FastAPI
from dynaconf import settings
from starlette.middleware.cors import CORSMiddleware
from app.restapi import api_router
from tortoise.contrib.fastapi import register_tortoise

# Import all modules from models
import importlib, glob
modules = []
for module in glob.glob("./app/models/*.py"):
    if "__" not in module:
        module = module[module.rfind("/")+1:module.rfind(".")]
        modules.append(importlib.import_module(f"app.models.{module}"))

# Create app
application = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION)

# Middlewares
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (endpoints)
application.include_router(api_router.router)

# Init Tortoise ORM and the app

register_tortoise(
    application,
    db_url=settings.POSTGRES_URI,
    modules={"models": modules},
    generate_schemas=True,
    add_exception_handlers = True
    )
