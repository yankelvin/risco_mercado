import numpy as np

# Suponha que você tenha uma carteira com os seguintes ativos e pesos
ativos = ["Ações", "Títulos", "Imóveis"]
pesos = [0.4, 0.3, 0.3]  # Porcentagem da carteira atribuída a cada ativo

# Suponha que você tenha os retornos históricos de cada ativo em uma estrutura de dados (por exemplo, listas ou arrays)
# Aqui, usarei listas de exemplos para os retornos
retornos_acoes = [0.05, 0.03, -0.02, 0.04, -0.01]  # Retornos históricos das ações
retornos_titulos = [0.02, 0.01, 0.03, -0.01, 0.02]  # Retornos históricos dos títulos
retornos_imoveis = [0.03, 0.02, 0.01, 0.02, 0.04]  # Retornos históricos dos imóveis

# Defina o número de simulações de Monte Carlo
num_simulacoes = 10000

# Realize simulação de Monte Carlo
simulacoes_carteira = []
for _ in range(num_simulacoes):
    # Simule os retornos dos ativos para o próximo período
    retornos_simulados = []
    for retorno_acao, retorno_titulo, retorno_imovel in zip(
        retornos_acoes, retornos_titulos, retornos_imoveis
    ):
        retornos_ativo = [retorno_acao, retorno_titulo, retorno_imovel]
        retorno_simulado = np.random.choice(retornos_ativo)
        retornos_simulados.append(retorno_simulado)

    # Calcule o retorno da carteira para o próximo período
    retorno_carteira = sum(
        retorno * peso for retorno, peso in zip(retornos_simulados, pesos)
    )
    simulacoes_carteira.append(retorno_carteira)

# Calcule o VaR
nivel_confianca = 0.95
var = np.percentile(simulacoes_carteira, 100 * (1 - nivel_confianca))
print("Value at Risk (VaR) em {}% de confiança:".format(nivel_confianca * 100), var)
