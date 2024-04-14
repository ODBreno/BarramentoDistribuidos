from flask import Flask, jsonify

app = Flask(__name__)

# Implementação da primeira ação
@app.route('/servicos', methods=['GET'])
def servico1(servico):
    if servico == 'mensagem':
        return jsonify({'mensagem': 'Mensagem recebida com sucesso!'})
    elif servico == 'arquivo':
        return jsonify({'mensagem': 'Arquivo alterado com sucesso!'})
    elif servico == 'calculo':
        return jsonify({'mensagem': 'Cálculo realizado com sucesso!'})
    
    else:
        return jsonify({'mensagem': 'Serviço não encontrado!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)