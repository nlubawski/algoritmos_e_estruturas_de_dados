# 2
# 1 | 2 | 4 | 5 | 6
# 1 | 2
# 2

resultado = -1
inicio = 0
fim = tamanho - 1
meio = 0
alvo = int(input("Digite o elemento a ser encontrado: "))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if (numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio] > alvo):
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print("Elemento não encontrado")
else:
    print(f"O elemento {alvo} está na posição {resultado}")