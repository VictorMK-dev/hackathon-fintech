# 📈 InvestFácil

> Plataforma educacional de investimentos desenvolvida na Hackathon de Calouros da UNAMA 2025.

---

## 👥 Integrantes

- Gustavo Pina(Pesquisa)
- Renato Valois(Frontend)
- Danilo(Frontend)
- Nicolas Rocha(Backend/.json)
- Victor Brandão(Backend/Frontend)

---

## 💡 Problema escolhido

Investir na bolsa de valores ainda intimida muita gente. A maioria das plataformas é complexa, cheia de termos técnicos e pouco acessível para quem está começando. Muitas pessoas evitam investir por não entender onde colocar o dinheiro ou por não conseguir acompanhar seus ativos de forma simples.

---

## 🚀 Solução proposta

O **InvestFácil** é um site que oferece:

- 📊 **Mercado de ativos** — acompanhe 19 ativos (ações, FIIs e Tesouro Direto) com classificações de compra, manutenção e venda
- 📈 **Índices de mercado** — visualize Ibovespa, IFIX, SMLL e IDIV em tempo real
- 🎯 **Perfil do investidor** — questionário de 4 perguntas com recomendação personalizada de carteira
- 🧮 **Simulador de carteira** — simule rendimentos em até 36 meses com distribuição customizável
- 📚 **Conteúdo educacional** — botão de acesso direto a vídeo introdutório sobre investimentos

---

## 🛠️ Tecnologias usadas

| Camada | Tecnologia |
|--------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python + Flask |
| Dados | Dados simulados (JSON) |
| Versionamento | Git + GitHub |

---

## 📁 Estrutura do projeto
investfacil/
├── backend/
│   ├── app.py           # API Flask com todas as rotas
│   ├── data.json        # Dados simulados dos ativos
│   └── requirements.txt
│
├── frontend/
│   ├── index.html       # Landing page
│   ├── dashboard.html   # Mercado de ativos
│   ├── perfil.html      # Perfil do investidor
│   ├── simulador.html   # Simulador de carteira
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── dashboard.js
│       ├── perfil.js
│       └── simulador.js
│
└── README.md

---

## ▶️ Como executar o projeto

### Pré-requisitos
- Python 3.10+
- VS Code com extensão Live Server

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/VictorMK-dev/hackathon-fintech
cd hackathon-fintech
```

**2. Instale as dependências:**
```bash
python -m pip install flask flask-cors
```

**3. Rode o backend:**
```bash
python backend/app.py
```

**4. Abra o frontend:**

Abra o arquivo `frontend/index.html` com o **Live Server** no VS Code.

> ⚠️ O Flask precisa estar rodando para o site funcionar!

---

## 🔗 Rotas da API

| Rota | Descrição |
|------|-----------|
| `GET /api/ativos` | Lista todos os ativos (ações, FIIs, Tesouro) |
| `GET /api/mercado` | Índices de mercado e resumo do dia |
| `GET /api/perfil/<tipo>` | Recomendação por perfil (conservador, moderado, arrojado) |

---

## ⚠️ Aviso

Os dados apresentados são **fictícios e simulados**, com fins exclusivamente educacionais. Não constituem recomendação de investimento.

---

*Desenvolvido na Hackathon de Calouros — UNAMA, Abril 2025*