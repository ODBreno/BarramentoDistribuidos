from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/servicos', methods=['POST'])
def servicos():
    data = request.json
    url_responde_mensagem = 'http://localhost:5002/mensagem'
    url_altera_arquivo = 'http://localhost:5005/alterarArquivo'
    url_calculo = 'http://localhost:5004/calcular'
    print(data)
    if 'servico' in data:
        servico = data['servico']
        if servico == 'mensagem':
            resposta = requests.get(url_responde_mensagem, json=data).json()
            print(resposta)
            if resposta:
                mensagem = resposta.get('resposta')
                return jsonify({'mensagem': mensagem})
        elif servico == 'arquivo':
            resposta = requests.get(url_altera_arquivo, json=data).json()
            if resposta:
                mensagem = resposta.get('mensagem')    
                return jsonify({'mensagem': mensagem})
        elif servico == 'calculo':
            resposta = requests.get(url_calculo, json=data).json()
            print(resposta)
            if resposta:
                resultado = resposta.get('resultado')    
                return jsonify({'resultado': resultado})
        else:
            return jsonify({'resultado': 'Serviço não encontrado!'})
    else:
        return jsonify({'resultado': 'Nenhum serviço enviado!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)