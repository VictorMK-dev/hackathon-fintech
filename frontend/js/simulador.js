function atualizarDistribuicao() {
  const acoes = parseInt(document.getElementById("range-acoes").value)
  const fiis = parseInt(document.getElementById("range-fiis").value)
  const rf = parseInt(document.getElementById("range-rf").value)
  const total = acoes + fiis + rf

  document.getElementById("val-acoes").textContent = acoes + "%"
  document.getElementById("val-fiis").textContent = fiis + "%"
  document.getElementById("val-rf").textContent = rf + "%"

  if (total !== 100) {
    document.getElementById("aviso-total").classList.remove("hidden")
  } else {
    document.getElementById("aviso-total").classList.add("hidden")
  }
}

function simular() {
  const valor = parseFloat(document.getElementById("valor-inicial").value)
  const meses = parseInt(document.getElementById("periodo").value)
  const acoes = parseInt(document.getElementById("range-acoes").value)
  const fiis = parseInt(document.getElementById("range-fiis").value)
  const rf = parseInt(document.getElementById("range-rf").value)
  const total = acoes + fiis + rf

  if (total !== 100) {
    document.getElementById("aviso-total").classList.remove("hidden")
    return
  }

  // Taxas mensais simuladas
  const taxaAcoes = 0.012   // ~14% ao ano
  const taxaFiis = 0.008    // ~10% ao ano
  const taxaRf = 0.009      // ~11% ao ano (Tesouro Selic)

  const rendAcoes = valor * (acoes / 100) * (Math.pow(1 + taxaAcoes, meses) - 1)
  const rendFiis = valor * (fiis / 100) * (Math.pow(1 + taxaFiis, meses) - 1)
  const rendRf = valor * (rf / 100) * (Math.pow(1 + taxaRf, meses) - 1)
  const rendTotal = rendAcoes + rendFiis + rendRf
  const valorFinal = valor + rendTotal

  const resultado = document.getElementById("simulador-resultado")
  resultado.innerHTML = `
    <div class="simulacao-resultado">
      <h2>Resultado da simulação — ${meses} meses</h2>
      <div class="resultado-numeros">
        <div class="num-card">
          <div class="num-card-label">Valor investido</div>
          <div class="num-card-value">R$ ${valor.toFixed(2)}</div>
        </div>
        <div class="num-card">
          <div class="num-card-label">Valor final estimado</div>
          <div class="num-card-value positive">R$ ${valorFinal.toFixed(2)}</div>
        </div>
        <div class="num-card">
          <div class="num-card-label">Rendimento total</div>
          <div class="num-card-value positive">+ R$ ${rendTotal.toFixed(2)}</div>
        </div>
        <div class="num-card">
          <div class="num-card-label">Rentabilidade</div>
          <div class="num-card-value positive">+ ${((rendTotal / valor) * 100).toFixed(1)}%</div>
        </div>
      </div>
      <div class="breakdown-title">Rendimento por categoria</div>
      <div class="breakdown-item"><span>📊 Ações (${acoes}%)</span><span>+ R$ ${rendAcoes.toFixed(2)}</span></div>
      <div class="breakdown-item"><span>🏢 FIIs (${fiis}%)</span><span>+ R$ ${rendFiis.toFixed(2)}</span></div>
      <div class="breakdown-item"><span>🏦 Renda Fixa (${rf}%)</span><span>+ R$ ${rendRf.toFixed(2)}</span></div>
    </div>
  `
}