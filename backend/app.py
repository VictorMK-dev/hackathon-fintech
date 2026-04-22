# arquivo principal do backend
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ativos')
def ativos():
    return jsonify({
        "ativos": [
            {"nome": "PETR4", "tipo": "ação", "preco": 38.52, "variacao": "+1.3%"},
            {"nome": "VALE3", "tipo": "ação", "preco": 68.90, "variacao": "-0.5%"},
            {"nome": "HGLG11", "tipo": "FII", "preco": 156.20, "variacao": "+0.8%"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)