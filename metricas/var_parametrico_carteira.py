import numpy as np
from scipy.stats import norm

# Suponha que você tenha os retornos históricos de cada ativo em uma matriz (linhas = ativos, colunas = períodos de tempo)
retornos_ativos = np.array(
    [
        [0.05, 0.03, -0.02, 0.04, -0.01],  # Retornos históricos das ações
        [0.02, 0.01, 0.03, -0.01, 0.02],  # Retornos históricos dos títulos
        [0.03, 0.02, 0.01, 0.02, 0.04],
    ]
)  # Retornos históricos dos imóveis

# Suponha que você tenha os pesos dos ativos na carteira
pesos = np.array([0.4, 0.3, 0.3])  # Porcentagem da carteira atribuída a cada ativo

# Calcule a média e a matriz de covariância dos retornos dos ativos
media_ativos = np.mean(retornos_ativos, axis=1)
matriz_correlacao = np.corrcoef(retornos_ativos)

# Calcule o retorno esperado da carteira
retorno_carteira = np.dot(pesos, media_ativos)

# Calcule o risco da carteira
risco_carteira = np.sqrt(np.dot(np.dot(pesos.T, matriz_correlacao), pesos))

# Calcule o VaR paramétrico
nivel_confianca = 0.95
z_score = norm.ppf(1 - nivel_confianca)
var_parametrico = retorno_carteira + z_score * risco_carteira

print(
    "Value at Risk (VaR) paramétrico em {}% de confiança:".format(
        nivel_confianca * 100
    ),
    var_parametrico,
)
