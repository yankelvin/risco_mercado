import numpy as np

retornos = [0.05, 0.03, 0.06, 0.02, 0.04]

# Valor investido no ativo ou mercado (por exemplo, $100,000)
valor_investido = 100000
retorno_medio = np.mean(retornos)

# Exposição ao investimento
exposicao = valor_investido * retorno_medio
print("Exposição ao investimento:", exposicao)
