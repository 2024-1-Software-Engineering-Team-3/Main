from flask import Flask
from config import Config
from models import db
from auth.__init__ import auth_bp
from recruitment.__init__ import recruit_bp
from qa.__init__ import qa_bp
# from document import document_bp
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/Login')
    app.register_blueprint(recruit_bp, url_prefix='/Recruitment')
    app.register_blueprint(qa_bp, url_prefix='/QA')
    # app.register_blueprint(document_bp, url_prefix='/document')

    @app.before_request
    def create_tables():
        db.create_all()

    return app
