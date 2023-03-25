from flask import Flask
from flask_bootstrap import Bootstrap

from backend.MainContainer import MainContainer
from backend.controllers import PhoneControllers


def create_app() -> Flask:
    container = MainContainer()

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", PhoneControllers.index)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    return app
