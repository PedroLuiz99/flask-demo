from hello_world.models.user_model import User
from hello_world.ext.database import db


def new_user(user):
    n_user = User()
    n_user.user_name = user['user_name']
    n_user.email = user['email']
    db.session.add(n_user)
    db.session.commit()

    return {"message": "Sucesso"}, 201


def list_users():
    return User.query.all()


def get_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()

    return None, 204
