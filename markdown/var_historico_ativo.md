# Cálculo do VaR (Value at Risk)

Neste documento, vamos explicar o cálculo do VaR (Value at Risk), que é uma medida de risco financeiro que quantifica a perda potencial em um investimento ou carteira em um determinado intervalo de tempo e nível de confiança.

## Passo 1: Definição dos Retornos Históricos

-   Os retornos históricos representam as variações nos preços de um ativo ao longo do tempo.
-   Por exemplo, suponha que temos os seguintes retornos históricos: [0.05, 0.03, 0.06, 0.02, 0.04].

## Passo 2: Especificação do Nível de Confiança

-   O nível de confiança é a probabilidade de que o VaR estimado seja maior ou igual à perda real.
-   Por exemplo, podemos especificar um nível de confiança de 95%.

## Passo 3: Ordenação dos Retornos

-   Os retornos históricos devem ser ordenados do menor para o maior.
-   Isso nos permite identificar o valor correspondente ao nível de confiança.
-   Usando o exemplo anterior, os retornos ordenados seriam: [0.02, 0.03, 0.04, 0.05, 0.06].

## Passo 4: Encontrar o Índice Correspondente ao Nível de Confiança

-   Multiplicamos o nível de confiança pelo número total de retornos.
-   Isso nos dá o índice correspondente ao nível de confiança na lista ordenada de retornos.
-   No exemplo, com 95% de confiança e 5 retornos, o índice correspondente seria 4 (5 \* 0.95 = 4.75).

## Passo 5: Calcular o VaR

-   O VaR é o retorno histórico no índice correspondente ao nível de confiança.
-   Para o exemplo dado, o VaR seria o quinto retorno na lista ordenada: 0.06.

Aqui está o código Python para calcular o VaR:

```python
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
```
