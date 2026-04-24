let todosAtivos = []

fetch("http://localhost:5000/api/ativos")
  .then(res => res.json())
  .then(dados => {
    todosAtivos = dados.ativos
    document.getElementById("loading").style.display = "none"
    renderizar(todosAtivos)
  })
  .catch(() => {
    document.getElementById("loading").textContent = "Erro ao conectar com o servidor."
  })

function renderizar(ativos) {
  const lista = document.getElementById("lista-ativos")
  lista.innerHTML = ""

  ativos.forEach(ativo => {
    const positivo = ativo.variacao.startsWith("+")
    lista.innerHTML += `
      <div class="ativo-card">
        <div class="ativo-header">
          <span class="ativo-nome">${ativo.nome}</span>
          <span class="ativo-tipo">${ativo.tipo}</span>
        </div>
        <div class="ativo-preco">R$ ${ativo.preco.toFixed(2)}</div>
        <div class="ativo-variacao ${positivo ? 'positive' : 'negative'}">${ativo.variacao}</div>
        <div class="ativo-desc">${ativo.descricao || ''}</div>
      </div>
    `
  })
}

function filtrar(tipo) {
  document.querySelectorAll(".filter-btn").forEach(btn => btn.classList.remove("active"))
  event.target.classList.add("active")

  if (tipo === "todos") {
    renderizar(todosAtivos)
  } else {
    renderizar(todosAtivos.filter(a => a.tipo === tipo))
  }
}