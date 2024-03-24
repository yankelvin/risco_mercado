# Cálculo da Volatilidade usando EWMA (Exponential Weighted Moving Average)

Neste documento, vamos explicar como calcular a volatilidade de um ativo financeiro usando o modelo EWMA. A volatilidade é uma medida estatística de dispersão dos retornos de um ativo ao longo do tempo.

## Passo 1: Definição dos Retornos

- Suponha que temos os retornos diários de um ativo financeiro em uma lista ou array: `retornos`.

## Passo 2: Conversão para uma Série Temporal

- Convertemos a lista de retornos em uma série temporal usando a biblioteca pandas.

## Passo 3: Cálculo da Volatilidade usando EWMA

- Escolhemos um período de suavização (número de períodos) e um fator de suavização.
- Usamos o método `ewm()` da série temporal para calcular a volatilidade usando o modelo EWMA.
- A volatilidade EWMA é calculada como o desvio padrão dos retornos ponderados exponencialmente.

Aqui está o código Python para calcular a volatilidade usando o modelo EWMA:

```python
import numpy as np
import pandas as pd

# Suponha que tenhamos os retornos diários de um ativo em uma lista ou array
retornos = [0.05, 0.03, 0.06, 0.02, 0.04, 0.01, -0.02, 0.03, -0.01, 0.02]

# Converter a lista de retornos em uma série pandas
serie_retornos = pd.Series(retornos)

# Calcular a volatilidade usando o modelo EWMA (Exponential Weighted Moving Average)
periodo_volatilidade = 10  # Número de períodos para calcular a volatilidade
fator_suavizacao = 0.94  # Fator de suavização

volatilidade_ewma = serie_retornos.ewm(span=periodo_volatilidade, min_periods=periodo_volatilidade).std().iloc[-1]

print("Volatilidade EWMA:", volatilidade_ewma)
