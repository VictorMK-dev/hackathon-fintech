// lógica do frontend
fetch("http://localhost:5000/api/ativos")
  .then(resposta => resposta.json())
  .then(dados => {
    const lista = document.getElementById("lista-ativos")
    lista.innerHTML = ""

    dados.ativos.forEach(ativo => {
      lista.innerHTML += `
        <div class="ativo">
          <h3>${ativo.nome}</h3>
          <p>Tipo: ${ativo.tipo}</p>
          <p>Preço: R$ ${ativo.preco}</p>
          <p>Variação: ${ativo.variacao}</p>
        </div>
      `
    })
  })