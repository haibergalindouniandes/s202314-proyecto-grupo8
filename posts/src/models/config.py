from os import environ as env


DB_USER = env['DB_USER']
DB_PASSWORD = env['DB_PASSWORD']
DB_HOST = env['DB_HOST']
DB_PORT = env['DB_PORT']
DB_NAME = env['DB_NAME']

def set_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True