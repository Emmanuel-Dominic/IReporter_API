from flask import Flask
from api.routes.user_route import user_bp
from api.routes.redflag_route import redflag_bp
from api.routes.intervention_route import intervention_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(redflag_bp)
app.register_blueprint(intervention_bp)
