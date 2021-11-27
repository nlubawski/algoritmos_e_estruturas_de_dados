# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1
# 1 | 2 | 4 | 6 | 5
# 1 | 2 | 4 | 5 | 6

# Melhor caso: N * N = N^2 O(n^2)
# Pior caso: N * N = N^2 O(n^2)
# Caso médio: N * N = N^2

for i in range(tamanho): # N
    indice_menor = i #5
    for j in range(int(i + 1), tamanho): # N
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor:", numeros)