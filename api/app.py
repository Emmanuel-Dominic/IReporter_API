from flask import Flask
# from api.views.intervention_view import intervention_bp
# from api.views.redflag_view import redflag_bp
from api.views.user_view import user_bp
from api.views.incident_view import incident_bp


app = Flask(__name__)

# app.register_blueprint(intervention_bp)
# app.register_blueprint(redflag_bp)
app.register_blueprint(user_bp)
app.register_blueprint(incident_bp)
