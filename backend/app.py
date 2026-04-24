from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Carrega os dados do arquivo JSON
def carregar_ativos():
    caminho = os.path.join(os.path.dirname(__file__), 'data', 'ativos.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

# Rota: lista todos os ativos
@app.route('/api/ativos')
def ativos():
    dados = carregar_ativos()
    return jsonify(dados)

# Rota: recomendação por perfil
@app.route('/api/perfil/<tipo>')
def perfil(tipo):
    perfis = {
        "conservador": {
            "nome": "Investidor Conservador",
            "descricao": "Você prefere segurança e previsibilidade. Seu foco é preservar o patrimônio com baixo risco, priorizando renda fixa e ativos estáveis.",
            "carteira": [
                {"tipo": "Tesouro Direto / Renda Fixa", "percentual": 70},
                {"tipo": "FIIs (Fundos Imobiliários)", "percentual": 20},
                {"tipo": "Ações", "percentual": 10}
            ]
        },
        "moderado": {
            "nome": "Investidor Moderado",
            "descricao": "Você busca equilíbrio entre segurança e crescimento. Aceita algum risco para ter retornos melhores no médio prazo.",
            "carteira": [
                {"tipo": "Tesouro Direto / Renda Fixa", "percentual": 40},
                {"tipo": "FIIs (Fundos Imobiliários)", "percentual": 30},
                {"tipo": "Ações", "percentual": 30}
            ]
        },
        "arrojado": {
            "nome": "Investidor Arrojado",
            "descricao": "Você tem alta tolerância ao risco e foco no longo prazo. Prioriza crescimento de patrimônio e aceita volatilidade pelo caminho.",
            "carteira": [
                {"tipo": "Ações", "percentual": 60},
                {"tipo": "FIIs (Fundos Imobiliários)", "percentual": 25},
                {"tipo": "Tesouro Direto / Renda Fixa", "percentual": 15}
            ]
        }
    }

    if tipo not in perfis:
        return jsonify({"erro": "Perfil inválido"}), 400

    return jsonify(perfis[tipo])

if __name__ == '__main__':
    app.run(debug=True)