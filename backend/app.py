from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


@app.route("/mercado")
def mercado():
    return jsonify(data["mercado"])


@app.route("/acoes")
def acoes():
    return jsonify(data["acoes"])


@app.route("/acoes/<ticker>")
def acao_por_ticker(ticker):
    acao = next((a for a in data["acoes"] if a["ticker"] == ticker.upper()), None)
    if not acao:
        return jsonify({"erro": "Ação não encontrada"}), 404
    return jsonify(acao)


@app.route("/fiis")
def fiis():
    return jsonify(data["fiis"])


@app.route("/fiis/<ticker>")
def fii_por_ticker(ticker):
    fii = next((f for f in data["fiis"] if f["ticker"] == ticker.upper()), None)
    if not fii:
        return jsonify({"erro": "FII não encontrado"}), 404
    return jsonify(fii)


@app.route("/tesouro")
def tesouro():
    return jsonify(data["tesouro_direto"])


@app.route("/perfil/<tipo>")
def perfil(tipo):
    perfis = data["perfis_investidor"]
    if tipo not in perfis:
        return jsonify({"erro": "Perfil inválido. Use: conservador, moderado ou arrojado"}), 400
    return jsonify(perfis[tipo])


@app.route("/carteiras")
def carteiras():
    return jsonify(data["carteiras_modelo"])


@app.route("/carteiras/<perfil_id>")
def carteira_por_perfil(perfil_id):
    carteira = next((c for c in data["carteiras_modelo"] if c["perfil"] == perfil_id), None)
    if not carteira:
        return jsonify({"erro": "Carteira não encontrada"}), 404
    return jsonify(carteira)


@app.route("/glossario")
def glossario():
    return jsonify(data["glossario"])


if __name__ == "__main__":
    app.run(debug=True)