from flask import Flask
from views.user_view import user_bp
from views.intervention_view import intervention_bp
from views.redflag_view import redflag_bp

app = Flask(__name__)

app.register_blueprint(intervention_bp)
app.register_blueprint(redflag_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
