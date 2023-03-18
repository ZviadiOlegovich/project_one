from flask import Blueprint

task_routes_bp = Blueprint('task_routes_bp', __name__, url_prefix='/tasks')