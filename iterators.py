"""
No Python, Iterators são objetos que permite que uma coleção de elementos seja percorrida sem a necessidade de qualquer
implementação, como o uso do for. Um Iterator possui, basicamente, dois métodos:

1 - O método __iter__() que inicializa e retorna o objeto a ser iterado;

2 - O método __next__() responsável por retornar o próximo elemento da sequência.

Com isso, o uso dos Iterators possui diversas vantagens, como:

Pode trabalhar com sequência infinitas, por não determinar a quantidade de saltos do loop;
Salva os elementos percorridos em sua memória.
Pode trabalhar com diversos tipos de estruturas sem mudar sua implementação, como Tuplas, Listas, Dicionários, etc.

"""