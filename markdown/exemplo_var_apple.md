# Cálculo do VaR Paramétrico usando yfinance

Neste documento, vamos explicar como calcular o Valor em Risco (VaR) Paramétrico usando a biblioteca yfinance para obter os dados históricos de um ativo financeiro.

## Passo 1: Importar as Bibliotecas Necessárias

- Utilizamos as bibliotecas `numpy` e `yfinance` para calcular o VaR Paramétrico e obter os dados históricos do ativo, respectivamente.

## Passo 2: Obtenção dos Dados Históricos do Ativo

- Definimos o ticker do ativo de interesse, por exemplo, `"AAPL"` para a Apple Inc.
- Utilizamos a função `yf.download()` do yfinance para obter os dados históricos do ativo para um período específico.

## Passo 3: Cálculo dos Retornos Diários

- Calculamos os retornos diários do ativo usando a função `pct_change()` no preço de fechamento ajustado (`"Adj Close"`) dos dados históricos.
- Removemos a primeira linha que contém um valor NaN (Not a Number).

## Passo 4: Cálculo do VaR Paramétrico

- Definimos o nível de confiança desejado, por exemplo, 95%.
- Calculamos o retorno médio e o desvio padrão dos retornos diários do ativo.
- Calculamos o valor crítico (Z-score) correspondente ao nível de confiança usando a função `np.percentile()` aplicada a uma distribuição normal.
- Finalmente, calculamos o VaR Paramétrico somando o retorno médio ao produto do Z-score pelo desvio padrão.

Aqui está o código Python para calcular o VaR Paramétrico usando yfinance:

```python
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
