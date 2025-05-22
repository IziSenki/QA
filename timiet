import timeit

# Versão com loop
def soma_loop():
    resultado = 0
    for i in range(10000):
        resultado += i
    return resultado

# Versão com sum()
def soma_builtin():
    return sum(range(10000))

# Medição
num_execucoes = 1000
tempo_loop = timeit.timeit(soma_loop, number=num_execucoes)
tempo_sum = timeit.timeit(soma_builtin, number=num_execucoes)

# Resultados formatados
print(f"\n⚡ Performance Comparison (média de {num_execucoes} execuções)")
print(f"• Loop for: {tempo_loop:.5f} segundos")
print(f"• sum():    {tempo_sum:.5f} segundos")
print(f"\nsum() é {tempo_loop/tempo_sum:.1f}x mais rápido que loop for")
