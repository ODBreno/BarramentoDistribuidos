from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/servicos', methods=['POST'])
def servicos():
    data = request.json
    url_responde_mensagem = 'http://localhost:5002/mensagem'
    url_calculo = 'http://localhost:5004/calcular'
    url_altera_arquivo = 'http://localhost:5005/alterarArquivo'
    url_le_arquivo = 'http://localhost:5006/lerArquivo'
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
            print(resposta)
            if resposta:
                mensagem = resposta.get('mensagem')    
                return jsonify({'mensagem': mensagem})
        elif servico == 'calculo':
            resposta = requests.get(url_calculo, json=data).json()
            print(resposta)
            if resposta:
                resultado = resposta.get('resultado')    
                return jsonify({'resultado': resultado})
        elif servico == 'adicionar':
            # Serviço composto para adicionar créditos
            # Leitura do saldo antigo
            compra = data.get('creditos')
            r1 = requests.get(url_le_arquivo, json=data).json()
            saldo_antigo = r1.get('saldo')
            print(r1)
            
            # Cálculo do novo saldo
            json_calculo = {
                'numero1': saldo_antigo, 
                'numero2': compra,
                'operador': '+'
            }
            r2 = requests.get(url_calculo, json=json_calculo).json()
            saldo_novo = r2.get('resultado')
            print(r2)
            
            # Registro do novo saldo e envio da resposta
            json_arquivo = {
                'nome_arquivo': data.get('cpf'), 
                'texto': saldo_novo
            }
            r3 = requests.get(url_altera_arquivo, json=json_arquivo).json()
            print(r3)
            return jsonify({'saldo': saldo_novo})
        else:
            return jsonify({'resultado': 'Serviço não encontrado!'})
    else:
        return jsonify({'resultado': 'Nenhum serviço enviado!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)