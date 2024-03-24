import numpy as np
import pandas as pd

# Suponha que tenhamos os retornos diários de um ativo em uma lista ou array
retornos = [0.05, 0.03, 0.06, 0.02, 0.04, 0.01, -0.02, 0.03, -0.01, 0.02]

# Converter a lista de retornos em uma série pandas
serie_retornos = pd.Series(retornos)

# Calcular a volatilidade usando o modelo EWMA (Exponential Weighted Moving Average)
periodo_volatilidade = 10  # Número de períodos para calcular a volatilidade
fator_suavizacao = 0.94  # Fator de suavização

volatilidade_ewma = (
    serie_retornos.ewm(span=periodo_volatilidade, min_periods=periodo_volatilidade)
    .std()
    .iloc[-1]
)

print("Volatilidade EWMA:", volatilidade_ewma)
