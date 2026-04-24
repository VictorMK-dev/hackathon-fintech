let respostas = []
let perguntaAtual = 1

function responder(pergunta, tipo) {
  respostas.push(tipo)
  
  if (pergunta < 4) {
    document.getElementById(`perg-${pergunta}`).classList.add("hidden")
    document.getElementById(`perg-${pergunta + 1}`).classList.remove("hidden")
    perguntaAtual++
  } else {
    mostrarResultado()
  }
}

function mostrarResultado() {
  const contagem = { conservador: 0, moderado: 0, arrojado: 0 }
  respostas.forEach(r => contagem[r]++)

  let perfil
  if (contagem.conservador >= 3) perfil = "conservador"
  else if (contagem.arrojado >= 3) perfil = "arrojado"
  else perfil = "moderado"

  fetch(`http://localhost:5000/api/perfil/${perfil}`)
    .then(res => res.json())
    .then(dados => {
      document.getElementById("questionario").classList.add("hidden")
      const resultado = document.getElementById("resultado")
      resultado.classList.remove("hidden")
      resultado.innerHTML = `
        <div class="resultado-titulo">Seu perfil é</div>
        <h2>${dados.nome}</h2>
        <p class="resultado-desc">${dados.descricao}</p>
        <div class="carteira-recomendada">
          <h3>Carteira recomendada</h3>
          ${dados.carteira.map(item => `
            <div class="carteira-item">
              <span class="carteira-item-nome">${item.tipo}</span>
              <span class="carteira-item-pct">${item.percentual}%</span>
            </div>
          `).join("")}
        </div>
        <button class="btn-refazer" onclick="reiniciar()">↩ Refazer questionário</button>
      `
    })
    .catch(() => {
      document.getElementById("questionario").classList.add("hidden")
      const resultado = document.getElementById("resultado")
      resultado.classList.remove("hidden")
      resultado.innerHTML = `<p style="color:var(--negative); font-family: var(--font-mono)">Erro ao conectar com o servidor.</p>`
    })
}

function reiniciar() {
  respostas = []
  perguntaAtual = 1
  for (let i = 1; i <= 4; i++) {
    document.getElementById(`perg-${i}`).classList.add("hidden")
  }
  document.getElementById("perg-1").classList.remove("hidden")
  document.getElementById("questionario").classList.remove("hidden")
  document.getElementById("resultado").classList.add("hidden")
}