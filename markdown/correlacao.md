# Cálculo da Correlação entre Ativos Financeiros

Neste documento, vamos explicar como calcular a correlação entre os retornos de dois ativos financeiros. A correlação é uma medida estatística que indica o grau de relação linear entre duas variáveis. No contexto financeiro, a correlação entre os retornos de dois ativos é importante para entender como eles se movem juntos.

## Passo 1: Definição dos Retornos dos Ativos

- Os retornos dos ativos representam as variações nos preços dos ativos ao longo do tempo.
- Suponha que temos os retornos históricos de dois ativos em arrays numpy: `retornos_ativo1` e `retornos_ativo2`.

## Passo 2: Cálculo da Correlação

- Utilizamos a função `np.corrcoef()` do numpy para calcular a correlação entre os retornos dos dois ativos.
- A função retorna uma matriz de correlação, e o valor que nos interessa está na posição [0, 1] (ou [1, 0], pois é simétrica), que representa a correlação entre os dois ativos.

Aqui está o código Python para calcular a correlação entre os retornos dos ativos:

```python
import numpy as np

# Retornos dos ativos
retornos_ativo1 = np.array([0.05, 0.03, -0.02, 0.04, -0.01])  # Retornos do Ativo 1
retornos_ativo2 = np.array([0.02, 0.01, 0.03, -0.01, 0.02])  # Retornos do Ativo 2

# Calcular a correlação entre os retornos dos ativos
correlacao = np.corrcoef(retornos_ativo1, retornos_ativo2)[0, 1]

print("Correlação entre os ativos:", correlacao)
