# Retornos históricos do investimento (lista ou array)
retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Nível de confiança (por exemplo, 95%)
nivel_confianca = 0.95

# Ordenar os retornos do menor para o maior
retornos_ordenados = sorted(retornos)

# Encontrar o índice correspondente ao nível de confiança
indice_confianca = int(nivel_confianca * len(retornos_ordenados))

# Calcular o VaR
var = retornos_ordenados[indice_confianca]
print("Value at Risk (VaR) em {}% de confiança:".format(nivel_confianca * 100), var)
