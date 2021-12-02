"""
Analise de Algoritmos (ou de complexidade de algoritmos)

Queremos saber como o tempo de execução e o consumo de memória é afetado por aumento da entrada.
Ou seja, queremos o tempo/memoria em funcao do tamanho da entrada n (geralmente nos interessa
n suficientemente grande).

Vou descrever aqui as principais funcoes assintoticas, que devemos sempre ter em mente

*---------------------------------------------------------------------------------------*
-   Constante | Logaritmica | Linear | Sublinear | Quadratica | Cubica  | Exponencial   -
-             |             |        |           |            |         |               -
-      1      |    log(n)   |   n    | n log(n)  |     n²     |   n³    |      2^n      -
*---------------------------------------------------------------------------------------*

---------> ordem crescente de complexidade
---------> log nesse contexto é sempre na base 2

Exemplo de alguns algoritmos clássicos e sua complexidade
Alguns deles serão implementados neste mesmo repositorio

Constante: operacoes aritmeticas basicas, expressoes booleanas, desvio condicionais, atribuicao de variaveis,
maximo em vetor ordenado, min em vetor ordenado, operacoes em pilha e fila

Logaritmica: busca binaria(em lista ordenada), inserção/remoção em Heap, busca em profundidade em arvores binarias
balanceadas

Linear: iteracoes, maximo/minimo/busca em lista nao ordenada, travessia em arvore

Sublinear: ordenacao complexa (Merge, Quick, Heap), ordenacao da lib padrao (uma vez que os melhores algoritmos
de ordenacao tem essa complexidade, e natural que as linguagens tenham essa complexidade em geral)

Quadratica: ordenacao simples (selection, insertion, buble sort), travessia de matrix quadrada (nxn),
iteracao dentro de outra iteracao

Cubica: multiplicacao padrao de matrizes

Exponencial: fibonatti recursivo simples, torre de hanoi


"""