from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/servicos', methods=['POST'])
def servicos():
    data = request.json
    url_responde_mensagem = 'http://localhost:5002'
    url_altera_arquivo = 'http://localhost:5003'
    url_calculo = 'http://localhost:5004'
    if 'servico' in data:
        servico = data['servico']
        if servico == 'mensagem':
            resposta = requests.get(url_responde_mensagem, json=data)
            if resposta.status_code == 200:
                mensagem = resposta.json().get('mensagem')
                return jsonify({'mensagem': mensagem})
        elif servico == 'arquivo':
            resposta = requests.get(url_altera_arquivo, json=data)
            if resposta.status_code == 200:
                mensagem = resposta.json().get('mensagem')    
                return jsonify({'mensagem': mensagem})
        elif servico == 'calculo':
            resposta = requests.get(url_altera_arquivo, json=data)
            if resposta.status_code == 200:
                resultado = resposta.json().get('resultado')    
                return jsonify({'resultado': resultado})
        else:
            return jsonify({'mensagem': 'Serviço não encontrado!'})
    else:
        return jsonify({'error': 'Nenhum serviço enviado!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)