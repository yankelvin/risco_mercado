# Cálculo do VaR usando Monte Carlo

Neste documento, vamos explicar o cálculo do VaR (Value at Risk) usando a abordagem de simulação Monte Carlo. O VaR é uma medida de risco financeiro que quantifica a perda potencial em um investimento ou carteira em um determinado intervalo de tempo e nível de confiança.

## Passo 1: Definição dos Retornos Históricos

- Os retornos históricos representam as variações nos preços de um ativo ao longo do tempo.
- Por exemplo, suponha que temos os seguintes retornos históricos: [0.05, 0.03, 0.06, 0.02, 0.04].

## Passo 2: Cálculo da Média e Desvio Padrão dos Retornos

- Calculamos a média e o desvio padrão dos retornos históricos.
- Isso nos fornece uma medida da tendência central e da dispersão dos retornos.
- Por exemplo, a média pode ser calculada usando `np.mean(retornos)` e o desvio padrão usando `np.std(retornos)`.

## Passo 3: Simulação Monte Carlo

- Utilizamos a simulação Monte Carlo para gerar múltiplos cenários de retornos.
- Simulamos retornos aleatórios seguindo uma distribuição normal com média igual à média dos retornos históricos e desvio padrão igual ao desvio padrão dos retornos históricos.
- No exemplo dado, estamos simulando 10.000 cenários de retornos.

## Passo 4: Ordenação dos Retornos Simulados

- Os retornos simulados são ordenados do menor para o maior.
- Isso nos permite identificar o valor correspondente ao nível de confiança.
- No exemplo, estamos usando um nível de confiança de 95%.

## Passo 5: Cálculo do VaR Monte Carlo

- O VaR Monte Carlo é o retorno simulado no índice correspondente ao nível de confiança.
- Para o exemplo dado, o VaR Monte Carlo é o retorno no índice correspondente ao 95º percentil dos retornos simulados.

Aqui está o código Python para calcular o VaR Monte Carlo:

```python
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
