from routes.home import home_route
from routes.client import client_route
from database.database import db
from database.models.client import Client


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(client_route, url_prefix="/clients")


def configure_db():
    db.connect()
    db.create_tables([Client])
