import numpy as np
from scipy.stats import norm

# Retornos históricos do investimento (lista ou array)
retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Nível de confiança (por exemplo, 95%)
nivel_confianca = 0.95

# Calcular a média e o desvio padrão dos retornos
media = np.mean(retornos)
volatilidade = np.std(retornos)

# Calcular o VaR paramétrico usando a distribuição normal
z_score = norm.ppf(1 - nivel_confianca)
var_parametrico = media + z_score * volatilidade
print(
    "VaR Paramétrico em {}% de confiança:".format(nivel_confianca * 100),
    var_parametrico,
)
