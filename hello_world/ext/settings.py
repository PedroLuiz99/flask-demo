from importlib import import_module


def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/d/DESENVOLVIMENTO/py_newbie/database.db'


def load_extensions(app, extensions):
    for extension in extensions:
        module, factory = extension.split(':')
        ext = import_module(module)
        getattr(ext, factory)(app)
