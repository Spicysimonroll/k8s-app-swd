from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify(message = 'Hello from K8S')

@app.route('/hostname')
def get_hostname():
    msg = os.getenv('MESSAGE', 'Hello from K8S')
    hostname = socket.gethostname()
    return jsonify(hostname = hostname, message = msg)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
