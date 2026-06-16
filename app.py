from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota 1: Página inicial (/) - Essencial para o teste do Render
@app.route('/', methods=['GET'])
def home():
    """Página inicial da API."""
    return jsonify({"message": "API do Robô Lendário está online!"})

# Rota 2: Verificação de Saúde (/health) - Outra rota comum para testes
@app.route('/health', methods=['GET'])
def health_check():
    """Rota de verificação de saúde para a plataforma de deploy."""
    return jsonify({"status": "healthy"}), 200

# Rota 3: Obter dados (/data) - Conforme seu README
@app.route('/data', methods=['GET'])
def get_data():
    """Exemplo de uma rota que retorna dados."""
    sample_data = {
        "id": 123,
        "name": "Legendary Octo Robot",
        "owner": "Dêleon"
    }
    return jsonify(sample_data)

# Rota 4: Echo (/api/echo) - Conforme seu README
@app.route('/api/echo', methods=['POST'])
def echo():
    """Retorna o mesmo JSON que foi enviado no corpo da requisição."""
    if not request.is_json:
        return jsonify({"error": "A requisição deve ser do tipo JSON"}), 400
    data = request.get_json()
    return jsonify(data)

# Rota 5: Sua rota original (/robot)
@app.route('/robot', methods=['GET'])
def robot():
    """Rota original do robô."""
    return jsonify({"status": "Robô lendário online"})

# Bloco para permitir execução local (boa prática)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)