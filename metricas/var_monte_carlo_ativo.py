import numpy as np

retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Calcular a média e o desvio padrão dos retornos
media = np.mean(retornos)
desvio_padrao = np.std(retornos)

# Definir o número de simulações
num_simulacoes = 10000

# Simular múltiplos cenários de retornos
retornos_simulados = np.random.normal(media, desvio_padrao, num_simulacoes)

# Ordenar os retornos simulados do menor para o maior
retornos_simulados_ordenados = np.sort(retornos_simulados)

# Nível de confiança (por exemplo, 95%)
nivel_confianca = 0.95

# Encontrar o índice correspondente ao nível de confiança
indice_confianca_mc = int(nivel_confianca * num_simulacoes)

# Calcular o VaR Monte Carlo
var_monte_carlo = retornos_simulados_ordenados[indice_confianca_mc]
print(
    "VaR Monte Carlo em {}% de confiança:".format(nivel_confianca * 100),
    var_monte_carlo,
)
