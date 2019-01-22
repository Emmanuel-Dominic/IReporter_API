from flask import Flask
from api.routes.user_route import user_bp
from api.routes.redflag_route import redflag_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(redflag_bp)


@app.route("/")
def index():
    return jsonify({"IReporter": "This enables any/every citizen to bring"
                " any form of corruption to the notice of appropriate"
                " authorities and the general public."}),200


    