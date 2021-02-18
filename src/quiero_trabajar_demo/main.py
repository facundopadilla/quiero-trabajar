from fastapi import FastAPI
from .models import db

from importlib.metadata import entry_points
def load_modules(app=None):
    for ep in entry_points()["quiero_trabajar_demo.modules"]:
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)

def get_app():
    app = FastAPI(title="Quiero trabajar")
    db.init_app(app)
    load_modules(app)
    return app