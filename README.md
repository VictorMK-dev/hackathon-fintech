# 📈 InvestFácil

> Site que facilita o acompanhamento e a tomada de decisão no mundo dos investimentos, tornando a bolsa de valores acessível para qualquer pessoa.

---

## 👥 Integrantes

- Rodrigo
- Gustavo
- Danilo (Frontend)
- Renato (Frontend)
- Nicolas (Backend)
- Victor (Backend)

---

## 💡 Problema escolhido

Investir na bolsa de valores é algo que ainda intimida muita gente. A maioria das plataformas existentes é complexa, cheia de termos técnicos e pouco acessível para quem está começando. Muitas pessoas evitam investir por não entender onde colocar o dinheiro ou por não conseguir acompanhar seus ativos de forma simples.

---

## 🚀 Solução proposta

O **InvestFácil** é um site que oferece:

- 📊 **Acompanhamento de ativos** — visualização clara de ações, FIIs e Tesouro Direto
- 🤖 **Sugestão de investimentos** — recomendação automática baseada no perfil do usuário (conservador, moderado ou arrojado)
- 📰 **Resumo do mercado** — visão geral do desempenho da bolsa de forma simples
- 💼 **Simulação de carteira** — o usuário monta uma carteira fictícia e vê como ela se comportaria

---

## 🛠️ Tecnologias usadas

| Camada    | Tecnologia        |
|-----------|-------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python + Flask    |
| Dados     | Dados simulados (JSON) |
| Versionamento | Git + GitHub |

---

## 📁 Estrutura do projeto

```
investfacil/
├── backend/
│   ├── app.py          # Arquivo principal da API Flask
│   ├── routes/
│   │   ├── ativos.py   # Rotas de ações, FIIs, Tesouro
│   │   └── perfil.py   # Rotas de recomendação por perfil
│   ├── data/
│   │   └── ativos.json # Dados simulados dos ativos
│   └── requirements.txt
│
├── frontend/
│   ├── index.html      # Landing page / apresentação
│   ├── dashboard.html  # Painel de acompanhamento
│   ├── perfil.html     # Questionário de perfil do investidor
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js     # Chamadas à API e lógica do frontend
│
└── README.md
```

---

## ▶️ Como executar o projeto

### Pré-requisitos
- Python 3.10+
- pip

### Passos

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/investfacil.git
cd investfacil
```

**2. Instale as dependências do backend:**
```bash
cd backend
pip install -r requirements.txt
```

**3. Rode o servidor Flask:**
```bash
python app.py
```

**4. Abra o frontend:**

Abra o arquivo `frontend/index.html` diretamente no navegador, ou use a extensão **Live Server** no VS Code.

---

## 📌 Observações

- Os dados de ativos são simulados — não há integração com APIs financeiras reais
- O projeto foi desenvolvido durante a Hackathon de Calouros da UNAMA (2025)
