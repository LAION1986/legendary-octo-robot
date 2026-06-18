from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN") 
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")

@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem":"API do Robô Lendário está online!"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status":"saudavel"}), 200

# ROTA NOVA DO WEBHOOK WHATSAPP
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge, 200
        return 'Token inválido', 403
    
    if request.method == 'POST':
        data = request.get_json()
        print("Dados WhatsApp:", data)
        return 'EVENT_RECEIVED', 200

@app.route('/robot', methods=['GET'])
def robot():
    return jsonify({"status":"Robô lendário online"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
