from flask import Blueprint
from flask_restful import Api
from .routes import DocumentCheck

document_bp = Blueprint('document', __name__)
api = Api(document_bp)

api.add_resource(DocumentCheck, '/Verify')
