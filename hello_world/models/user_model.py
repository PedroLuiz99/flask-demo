from hello_world.ext.database import db
from hello_world.ext.marshmallow import marshmallow


class User(db.Model):
    """Model de usuário"""

    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_schema = True
