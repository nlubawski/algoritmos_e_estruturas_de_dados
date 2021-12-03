"""A busca linear (ou busca sequencial) é um tipo de pesquisa em vetores ou listas
 elemento por elemento, de modo que a função do tempo em relação ao número de elementos é linear.
 Podemos observar que no melhor caso, o elemento a ser buscado é encontrado
na primeira tentativa. No pior caso o elemento a ser
buscado encontra-se na última posição, dessa forma temos n comparações.
O caso medio e dado por (n+1)/2 comparações. O algoritmo de busca linear é um algoritmo O(n).
"""

pesquisar = int(input("Digite o valor a ser pesquisado no vetor: "))
posicao_resultado = -1
for i in range(tamanho):
    if numeros[i] == pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print("O elemento não foi encontrado no vetor")
else:
    print(f"Elemento encontrado na posição {posicao_resultado}")
