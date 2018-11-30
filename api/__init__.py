from flask import Flask, jsonify
# from api.views.user_view import user_bp
from api.views.intervention_view import intervention_bp
from api.views.redflag_view import redflag_bp

app = Flask(__name__)

app.register_blueprint(intervention_bp)
app.register_blueprint(redflag_bp)
# app.register_blueprint(user_bp)

if __name__ == ('__main__'):
    app.run()
