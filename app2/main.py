from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from App2 (Backend)!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
