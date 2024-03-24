import numpy as np

# Retornos dos ativos
retornos_ativo1 = np.array([0.05, 0.03, -0.02, 0.04, -0.01])  # Retornos do Ativo 1
retornos_ativo2 = np.array([0.02, 0.01, 0.03, -0.01, 0.02])  # Retornos do Ativo 2

# Calcular a correlação entre os retornos dos ativos
correlacao = np.corrcoef(retornos_ativo1, retornos_ativo2)[0, 1]

print("Correlação entre os ativos:", correlacao)
