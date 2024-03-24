# Cálculo da Exposição ao Investimento

Neste documento, vamos explicar como calcular a exposição ao investimento com base nos retornos de um ativo ou mercado financeiro. A exposição representa o valor monetário investido em um ativo ou mercado.

## Passo 1: Definição dos Retornos do Ativo ou Mercado

- Os retornos do ativo ou mercado representam as variações nos preços ao longo do tempo.
- Suponha que temos os retornos históricos do ativo ou mercado em uma lista: `retornos`.

## Passo 2: Definição do Valor Investido

- O valor investido é a quantidade de dinheiro colocada no ativo ou mercado.
- Por exemplo, suponha que investimos $100,000 no ativo ou mercado.

## Passo 3: Cálculo da Exposição

- Multiplicamos o valor investido pelo retorno médio do ativo ou mercado para obter a exposição.
- O retorno médio é calculado como a média dos retornos históricos.
- A exposição representa o valor monetário exposto ao ativo ou mercado.

Aqui está o código Python para calcular a exposição ao investimento:

```python
import numpy as np

retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Valor investido no ativo ou mercado (por exemplo, $100,000)
valor_investido = 100000
retorno_medio = np.mean(retornos)

# Exposição ao investimento
exposicao = valor_investido * retorno_medio
print("Exposição ao investimento:", exposicao)
