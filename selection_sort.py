"""
O selection sort é um algoritmo de ordenação baseado em se passar sempre o menor valor do vetor
para a primeira posição, depois o de segundo menor valor para a segunda posição, e assim
sucessivamente.
É interessante notar que esse algortimo compara a cada iteracao um elemento com os outros,
de forma que no final ele vai ter percorrido os dois laços por completo, independente de termos
um vetor desordenado ou um ja ordenado. Por conta disso o pior caso se equivale ao melhor,
consequente o caso medio também é o mesmo, ou seja, O(n²).
"""

for i in range(tamanho):
    indice_menor = i
    for j in range(int(i + 1), tamanho):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor:", numeros)