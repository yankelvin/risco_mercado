# Cálculo do VaR Paramétrico para uma Carteira de Ativos

Neste documento, vamos explicar o cálculo do VaR (Value at Risk) paramétrico para uma carteira de ativos. O VaR é uma medida de risco financeiro que quantifica a perda potencial em um investimento ou carteira em um determinado intervalo de tempo e nível de confiança.

## Passo 1: Definição dos Retornos Históricos dos Ativos

- Os retornos históricos representam as variações nos preços de cada ativo ao longo do tempo.
- Suponha que temos os retornos históricos de cada ativo em uma matriz, onde as linhas representam os ativos e as colunas representam os períodos de tempo.

## Passo 2: Definição dos Pesos da Carteira

- Os pesos dos ativos na carteira indicam a porcentagem da carteira atribuída a cada ativo.
- Por exemplo, suponha que temos os seguintes pesos: [0.4, 0.3, 0.3], onde 40% para ações, 30% para títulos e 30% para imóveis.

## Passo 3: Cálculo da Média e Covariância dos Retornos dos Ativos

- Calculamos a média dos retornos de cada ativo para obter o retorno esperado.
- Calculamos a matriz de covariância dos retornos dos ativos para medir o relacionamento entre eles.
- Por exemplo, podemos usar `np.mean(retornos_ativos, axis=1)` para calcular a média dos retornos e `np.corrcoef(retornos_ativos)` para calcular a matriz de correlação.

## Passo 4: Cálculo do Retorno e Risco da Carteira

- Utilizamos os pesos da carteira, a média dos retornos dos ativos e a matriz de correlação para calcular o retorno esperado e o risco da carteira.
- O retorno esperado da carteira é calculado como o produto escalar dos pesos da carteira e a média dos retornos dos ativos.
- O risco da carteira é calculado como a raiz quadrada do produto escalar dos pesos da carteira, a matriz de correlação e os pesos da carteira.

## Passo 5: Cálculo do VaR Paramétrico

- Utilizamos a distribuição normal para calcular o VaR paramétrico da carteira.
- Calculamos o Z-score associado ao nível de confiança desejado usando `norm.ppf(1 - nivel_confianca)`.
- Multiplicamos o Z-score pelo risco da carteira e adicionamos ao retorno esperado da carteira para obter o VaR paramétrico.
- Por exemplo, o código Python para calcular o VaR paramétrico seria:

```python
import numpy as np
from scipy.stats import norm

# Suponha que você tenha os retornos históricos de cada ativo em uma matriz (linhas = ativos, colunas = períodos de tempo)
retornos_ativos = np.array(
    [
        [0.05, 0.03, -0.02, 0.04, -0.01],  # Retornos históricos das ações
        [0.02, 0.01, 0.03, -0.01, 0.02],  # Retornos históricos dos títulos
        [0.03, 0.02, 0.01, 0.02, 0.04],    # Retornos históricos dos imóveis
    ]
)  

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
