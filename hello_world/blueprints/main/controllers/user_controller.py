from flask import request
from flask_restx import Resource
from hello_world.utils.user_dto import UserDto
from hello_world.blueprints.main.service.user_service import new_user, list_users, get_user, delete_user
from hello_world.models.user_model import UserSchema

api = UserDto.api

_hello_world = UserDto.user


@api.route("/")
class UserController(Resource):
    def get(self):
        """Listar usuários"""
        schema = UserSchema(many=True)
        users = list_users()
        return schema.dump(users)

    @api.expect(_hello_world)
    def post(self):
        """Cadastrar um nome"""
        user_schema = UserSchema(exclude=['user_id'])
        errors = user_schema.validate(request.json)
        if errors:
            return {"message": "Corpo inválido", "validation": errors}, 400

        return new_user(request.json)

    def patch(self):
        """Modificar usuário"""
        pass


@api.route("/<user_id>")
class UserOperations(Resource):
    def get(self, user_id):
        """Buscar usuário por ID
        Se não encontrado, retorna vazio
        """
        return UserSchema().dump(get_user(user_id))

    def delete(self, user_id):
        """Remover usuário"""
        return delete_user(user_id)
