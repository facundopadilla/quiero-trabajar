from glob import glob
from importlib import import_module
from dynaconf import settings

modules = []
for module in glob("../models/*.py"):
    if "__" not in module:
        module = module[module.rfind("/")+1:module.rfind(".")]
        modules.append(import_module(f"app.models.{module}"))

modules.append("aerich.models")

TORTOISE_ORM = {
        "connections": {
            "default": settings.POSTGRES_URI
            },
        "apps": {
            "models": {
                "models": modules,
                "default_connection": "default",
            },
        }
    }
