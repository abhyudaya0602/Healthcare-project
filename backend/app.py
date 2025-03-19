from flask import Flask
from flask_cors import CORS
from routes import api_routes  # Ensure routes are imported

app = Flask(__name__)
CORS(app)  # 🔥 Fix: Allow Cross-Origin Requests

app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")