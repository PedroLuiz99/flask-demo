from flask import Flask
from hello_world.ext import settings


def create_app():
    app = Flask(__name__)
    settings.init_app(app)

    settings.load_extensions(app, [
        'hello_world.ext.database:init_app',
        'hello_world.ext.marshmallow:init_app',
        'hello_world.blueprints.main:init_app'
    ])
    return app
