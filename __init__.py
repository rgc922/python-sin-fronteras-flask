import os

from flask import Flask


### siempre es necesario cuando se trabaja con flask

def create_app():
    app = Flask(__name__)   

    app.config.from_mapping(
        ## ESTA ES PARA GENERAR IDENTIFICAR DEL USUARIO
        ## CON UNA COOKIE PARA CREAR SESIÓN
        SECRET_KEY = 'mikey', # en produccion debe ser mas compleja

        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE')
    )

    ### aquí arranca la applicación con la db
    from . import db
    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    ### ruta de prueabs
    @app.route('/hola')
    def hola():
        return 'Chanchito feliz funcion HOLA'

    return app