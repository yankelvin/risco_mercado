import numpy as np
import yfinance as yf

# Defina o ticker do ativo de interesse
ticker = "AAPL"  # Exemplo: Apple Inc.

# Obtenha os dados históricos do ativo
dados_ativo = yf.download(ticker, start="2024-01-01", end="2024-03-01")

# Calcule os retornos diários
dados_ativo["Retornos"] = dados_ativo["Adj Close"].pct_change()

# Remova a primeira linha (NaN)
dados_ativo = dados_ativo.dropna()

# Defina o nível de confiança desejado (por exemplo, 95%)
nivel_confianca = 0.95

# Calcule o retorno médio e o desvio padrão dos retornos
retorno_medio = dados_ativo["Retornos"].mean()
desvio_padrao = dados_ativo["Retornos"].std()

# Calcule o valor crítico (Z-score) correspondente ao nível de confiança
z_score = np.percentile(np.random.normal(size=len(dados_ativo)), nivel_confianca * 100)

# Calcule o VaR paramétrico
var_parametrico = retorno_medio + z_score * desvio_padrao

print(
    "Valor em Risco (VaR) paramétrico em {}% de confiança:".format(
        nivel_confianca * 100
    ),
    var_parametrico,
)
