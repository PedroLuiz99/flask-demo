from flask import Blueprint
from flask_restx import Api

from hello_world.blueprints.main.controllers.user_controller import api as user_ns

bp = Blueprint('api', __name__)

api = Api(
    bp,
    title="API Hello World",
    version="0.0.1",
    description="Apenas um hello world",
    doc="/docs"
)

api.add_namespace(user_ns, path="/hello")


def init_app(app):
    app.register_blueprint(bp, url_prefix='/api')
