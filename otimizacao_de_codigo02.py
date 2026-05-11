import numpy as np
import time

# ANTES
inicio = time.time()
soma = 0
for i in range (10**6):
    soma += i
fim = time.time()
print(fim - inicio, "segundos")

# DEPOIS
inicio = time.time()
soma_np = np.sum(np.arange(10**6))
fim = time.time()
print(fim - inicio, "segundos")

# Mais otimização:
n = 10**6
inicio = time.time()
soma = n * (n-1) / 2
fim = time.time()
print(fim - inicio, "segundos")

print(soma)