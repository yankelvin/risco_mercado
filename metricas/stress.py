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
