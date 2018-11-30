from flask import Flask, jsonify
# from api.views.user_view import user_bp
from api.views.incident_view import incident_bp

app = Flask(__name__)

app.register_blueprint(incident_bp)
# app.register_blueprint(user_bp)

if __name__ == ('__main__'):
    app.run()
