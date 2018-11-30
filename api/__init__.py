from flask import Flask, jsonify
# from api.views.auth_user import auth_blueprint
from api.views.incident_view import incident_bp

app = Flask(__name__)

# app.register_blueprint(auth_blueprint)
app.register_blueprint(incident_bp)


if __name__ == ('__main__'):
    app.run()
