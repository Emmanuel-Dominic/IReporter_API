from flask import Flask, jsonify
from app.views.incident_view import incident_bp

app = Flask(__name__)

@app.route('/')
def index():
   return jsonify({'Message': "Hello Ireporter"}), 200
    

app.register_blueprint(incident_bp)


if __name__ == ('__main__'):
    app.run()