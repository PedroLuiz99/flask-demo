from flask_restx import Namespace, fields


class UserDto:
    """DTO Exemplo"""
    api = Namespace("User", description="Teste")

    user = api.model('user', {
        'user_id': fields.Integer(required=True, description="ID do usuário"),
        'user_name': fields.String(required=True, description="Nome do usuário"),
        'email': fields.String(required=True, description="Email do usuário"),
    })
