from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/servicos', methods=['POST'])
def servicos():
    data = request.json
    
    if 'servico' in data:
        servico = data['servico']
        if servico == 'mensagem':
            mensagem = data['mensagem']
            if mensagem:
                return jsonify({'mensagem': f'Mensagem "{mensagem}" recebida com sucesso!'})
            else:
                return jsonify({'mensagem': 'Nenhuma mensagem recebida!'})
        elif servico == 'arquivo':
            return jsonify({'mensagem': 'Arquivo alterado com sucesso!'})
        elif servico == 'calculo':
            return jsonify({'mensagem': 'Cálculo realizado com sucesso!'})
    else:
        return jsonify({'mensagem': 'Serviço não encontrado!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)