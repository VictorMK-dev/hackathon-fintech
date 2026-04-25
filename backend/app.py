from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def carregar_dados():
    caminho = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

# Todos os ativos juntos
@app.route('/api/ativos')
def ativos():
    dados = carregar_dados()
    todos = []
    for a in dados['acoes']:
        todos.append({
            "nome": a['ticker'],
            "tipo": "ação",
            "preco": a['preco_atual'],
            "variacao": f"{'+' if a['variacao_dia'] >= 0 else ''}{a['variacao_dia']}%",
            "descricao": f"{a['nome']} — {a['setor']}. {a['motivo_classificacao']}",
            "classificacao": a['classificacao'],
            "nota": a['nota_sistema'],
            "dividend_yield": a.get('dividend_yield', 0),
            "adequado_para": a['adequado_para']
        })
    for f in dados['fiis']:
        todos.append({
            "nome": f['ticker'],
            "tipo": "FII",
            "preco": f['preco_atual'],
            "variacao": f"{'+' if f['variacao_dia'] >= 0 else ''}{f['variacao_dia']}%",
            "descricao": f"{f['nome']} — {f['segmento']}. {f['motivo_classificacao']}",
            "classificacao": f['classificacao'],
            "nota": f['nota_sistema'],
            "dividend_yield": f.get('dividend_yield_ano', 0),
            "adequado_para": f['adequado_para']
        })
    for t in dados['tesouro_direto']:
        todos.append({
            "nome": t['nome'],
            "tipo": "renda_fixa",
            "preco": t['rentabilidade_bruta_ano'],
            "variacao": "+0.0%",
            "descricao": f"{t['indicado_para']}. {t['motivo_classificacao']}",
            "classificacao": t['classificacao'],
            "nota": t['nota_sistema'],
            "dividend_yield": 0,
            "adequado_para": t['adequado_para']
        })
    return jsonify({"ativos": todos})

# Mercado — índices e resumo do dia
@app.route('/api/mercado')
def mercado():
    dados = carregar_dados()
    return jsonify(dados['mercado'])

# Perfil do investidor
@app.route('/api/perfil/<tipo>')
def perfil(tipo):
    dados = carregar_dados()
    perfis_raw = dados['perfis_investidor']
    carteiras = {c['perfil']: c for c in dados['carteiras_modelo']}

    if tipo not in perfis_raw:
        return jsonify({"erro": "Perfil inválido"}), 400

    p = perfis_raw[tipo]
    c = carteiras.get(tipo, {})

    return jsonify({
        "nome": f"Investidor {p['label']} {p['emoji']}",
        "descricao": p['descricao'],
        "horizonte": p['horizonte_tipico'],
        "frase": p['frase'],
        "rentabilidade_estimada": c.get('rentabilidade_estimada_ano', 0),
        "carteira": [
            {"tipo": "Renda Fixa / Tesouro", "percentual": p['alocacao_sugerida']['renda_fixa']},
            {"tipo": "FIIs", "percentual": p['alocacao_sugerida']['fiis']},
            {"tipo": "Ações", "percentual": p['alocacao_sugerida']['acoes']}
        ],
        "ativos_recomendados": p['ativos_recomendados']
    })

# Glossário
@app.route('/api/glossario')
def glossario():
    dados = carregar_dados()
    return jsonify(dados['glossario'])

if __name__ == '__main__':
    app.run(debug=True)