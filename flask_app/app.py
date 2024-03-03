from flask_app.config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    from flask_app.route_map import views as map_views
    
    app.register_blueprint(map_views.route_map, url_prefix='/map')

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
