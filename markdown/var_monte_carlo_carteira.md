# Cálculo do VaR usando Simulação de Monte Carlo para uma Carteira de Ativos

Neste documento, vamos explicar o cálculo do VaR (Value at Risk) usando simulação de Monte Carlo para uma carteira de ativos. O VaR é uma medida de risco financeiro que quantifica a perda potencial em um investimento ou carteira em um determinado intervalo de tempo e nível de confiança.

## Passo 1: Definição dos Ativos e Pesos da Carteira

- Os ativos representam os diferentes instrumentos de investimento na carteira.
- Os pesos indicam a porcentagem da carteira atribuída a cada ativo.
- Por exemplo, suponha que temos os seguintes ativos e pesos: Ações (40%), Títulos (30%), e Imóveis (30%).

## Passo 2: Definição dos Retornos Históricos dos Ativos

- Os retornos históricos representam as variações nos preços de cada ativo ao longo do tempo.
- Suponha que temos os retornos históricos de cada ativo em listas: retornos_acoes, retornos_titulos e retornos_imoveis.

## Passo 3: Simulação de Monte Carlo

- Realizamos simulação de Monte Carlo para gerar múltiplos cenários de retornos para a carteira.
- Para cada simulação, simulamos os retornos dos ativos para o próximo período.
- Calculamos o retorno da carteira para o próximo período somando os retornos ponderados dos ativos.

## Passo 4: Cálculo do VaR

- Calculamos o VaR com base nos retornos simulados da carteira.
- Por exemplo, para um nível de confiança de 95%, o VaR é o percentil correspondente no conjunto de retornos simulados.

Aqui está o código Python para calcular o VaR usando simulação de Monte Carlo:

```python
import numpy as np

# Suponha que você tenha uma carteira com os seguintes ativos e pesos
ativos = ["Ações", "Títulos", "Imóveis"]
pesos = [0.4, 0.3, 0.3]  # Porcentagem da carteira atribuída a cada ativo

# Suponha que você tenha os retornos históricos de cada ativo em listas
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
