"""
Vetor é uma estrutura básica que é um espaço de memória geralmente contínuo e segmentado,
onde cada posição de memória originada da segmentação pode ser utilizada para armazenar um elemento.

Quando falamos em vetores, eles geralmente armazenam o mesmo tipo de dado em todas segmentações. Alem disso
possuem um tamanho pré-determinado e acessamos as posicoes atraves de um indice numérico que começa em 0.

Em alguns lugares vetor = array unidimensional, matriz = array bidimensional. Outra coisa, dependendo da linguagem
podemos ter tanto a estrutura vetor quanto array, então vale sempre olhar a documentacao. O objetivo aqui e
aprensentar algoritmos classicos, principalmente de busca e ordenacao. Para isso usaremos a estrutura de vetor
construida a seguir.

"""
numeros = list()
tamanho = int(input('Digite o tamanho do vetor: '))
for i in range(tamanho):
    valor = int(input(f'Digite o número do vetor na posição {i}: '))
    numeros.append(valor)

#exibindo nosso vetor
print('Vetor: ', numeros)
