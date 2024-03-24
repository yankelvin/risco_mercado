# Cálculo do VaR Paramétrico

Neste documento, vamos explicar o cálculo do VaR (Value at Risk) paramétrico, que é uma medida de risco financeiro que quantifica a perda potencial em um investimento ou carteira em um determinado intervalo de tempo e nível de confiança, utilizando a distribuição normal.

## Passo 1: Definição dos Retornos Históricos

- Os retornos históricos representam as variações nos preços de um ativo ao longo do tempo.
- Por exemplo, suponha que temos os seguintes retornos históricos: [0.05, 0.03, 0.06, 0.02, 0.04].

## Passo 2: Especificação do Nível de Confiança

- O nível de confiança é a probabilidade de que o VaR estimado seja maior ou igual à perda real.
- Por exemplo, podemos especificar um nível de confiança de 95%.

## Passo 3: Cálculo da Média e Volatilidade dos Retornos

- Calculamos a média e o desvio padrão dos retornos históricos.
- Isso nos fornece uma medida da tendência central e da dispersão dos retornos.
- Por exemplo, a média pode ser calculada usando `np.mean(retornos)` e a volatilidade usando `np.std(retornos)`.

## Passo 4: Cálculo do VaR Paramétrico

- Utilizamos a distribuição normal para calcular o VaR paramétrico.
- Calculamos o Z-score associado ao nível de confiança desejado usando `norm.ppf(1 - nivel_confianca)`.
- Multiplicamos o Z-score pela volatilidade e adicionamos à média para obter o VaR paramétrico.
- O VaR paramétrico é uma estimativa da perda máxima esperada com base na distribuição normal dos retornos.
- Por exemplo, o código Python para calcular o VaR paramétrico seria:

```python
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
