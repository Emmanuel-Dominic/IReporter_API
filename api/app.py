from flask import Flask
from api.views.user_view import user_bp
from api.views.incident_view import incident_bp


app = Flask(__name__)


app.register_blueprint(user_bp)
app.register_blueprint(incident_bp)
