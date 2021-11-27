
# Melhor caso: 1 vez O(1)
# Pior caso: N vezes O(n)
# Caso médio: n/2 vezes

numero_pesquisar = int(input("Digite o valor a ser pesquisado no vetor: ")) #2
posicao_resultado = -1
for i in range(tamanho):
    # 0 .. 5
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print("O elemento não foi encontrado no vetor")
else:
    print(f"Elemento encontrado na posição {posicao_resultado}")
