import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from iqoptionapi.stable_api import IQ_Option

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Suas credenciais e SSID
SSID = "A_OEQ0BLQUmg239qW"

@app.route('/')
def index():
    return "Ponte IQ Option Ativa!"

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado à ponte IQ Option")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
