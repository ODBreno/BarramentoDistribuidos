from flask import Flask, jsonify

app = Flask(__name__)

# Implementação da primeira ação
@app.route('/servico1', methods=['GET'])
def servico1():
    # Lógica da primeira ação
    return jsonify({'mensagem': 'Ação 1 executada com sucesso'})

# Implementação da segunda ação
@app.route('/servico2', methods=['GET'])
def servico2():
    # Lógica da segunda ação
    return jsonify({'mensagem': 'Ação 2 executada com sucesso'})

# Implementação da terceira ação
@app.route('/servico3', methods=['GET'])
def servico33():
    # Chamada da aplicação que realiza o serviço 3
    return jsonify({'mensagem': 'Ação 3 executada com sucesso'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)