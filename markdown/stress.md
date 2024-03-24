# Simulação de Cenário de Estresse nos Retornos

Neste documento, vamos explicar como simular um cenário de estresse nos retornos de um investimento e calcular o retorno médio após esse cenário. Um cenário de estresse é uma situação hipotética que representa condições extremas de mercado.

## Passo 1: Definição dos Retornos do Investimento

- Os retornos do investimento representam as variações nos preços ao longo do tempo.
- Suponha que temos os retornos históricos do investimento em uma lista: `retornos`.

## Passo 2: Simulação do Cenário de Estresse

- Criamos uma função chamada `simulate_stress_scenario` que simula o impacto de um cenário de estresse nos retornos.
- O cenário de estresse é aplicado multiplicando os retornos originais por um fator de estresse.
- Suponha que queremos simular um cenário de estresse onde os retornos são reduzidos em 20% (fator de estresse = 0.8).

## Passo 3: Cálculo do Retorno Médio Após o Estresse

- Após aplicar o cenário de estresse, calculamos o retorno médio dos retornos estressados.
- Isso nos dá uma ideia do impacto do cenário de estresse no retorno médio do investimento.

Aqui está o código Python para simular um cenário de estresse nos retornos e calcular o retorno médio após esse cenário:

```python
import numpy as np

retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Suponha que você tenha uma função que simule o impacto de um cenário de estresse nos retornos
def simulate_stress_scenario(retornos, stress_factor):
    # Simulação do impacto do cenário de estresse nos retornos
    retornos_stress = [retorno * stress_factor for retorno in retornos]
    return retornos_stress

# Suponha que 'retornos' seja a lista de retornos do exemplo anterior
# Vamos simular um cenário de estresse onde os retornos são reduzidos em 20%
retornos_stress = simulate_stress_scenario(retornos, 0.8)

# Calcule o retorno médio após o cenário de estresse
retorno_medio_stress = np.mean(retornos_stress)
print("Retorno médio após cenário de estresse:", retorno_medio_stress)
