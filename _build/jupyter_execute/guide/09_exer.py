# Exercícios

1.1. Calcule a área de um círculo de raio 2. Assuma *pi = 3.14*. 

pass

1.2. Escreva uma função que verifica se um número é par. Se for, imprima uma mensagem. Se não for, imprima outra mensagem.

pass

1.3. No exercício acima, se o número for par, verifique se ele é múltiplo de 4. Se for, exiba uma mensagem diferente.

pass

1.4. Escreva um código que imprima os elementos menores que 5 na seguinte lista:

a = [1, 4, 2, 3, 2, 1, 5, 8, 5, 7, -1, 0, 23]

1.5. Escreva um código que encontra todos os divisores do número 42.

pass

1.6. Calcule a multiplicação das duas matrizes abaixo sem usar laços:

a = [[2, 3], [4, 2]]
b = [[2, 0], [1, 2]]

1.7. Calcule a multiplicação das duas matrizes acima usando laços

pass

1.8. Calcule o fatorial de 5 usando algum tipo de laço.

pass

1.9. Dada uma variável $X \sim N(0, 4)$, calcule o valor da fdp para o valor 2.

pass

1.10. Calcule a distância Euclidiana dos seguintes vetores:

a, b = [1, 0, 1], [-1, 2, 3]

1.11. Imprima as potências de 2, começando em $2^0$, enquanto o resultado for menor do que 2000.

pass

1.12. Verifique se o número 79 é primo.

pass

1.13. Escreva uma linha de código Python que gere uma lista apenas com os valores divisíveis por 2 e por 5 na lista abaixo:

a = [1, 4, 10, 13, 15, 16, 20, 28, 30]

1.14. Escreva um laço que resulte no sétimo elemento da [sequência de Fibonacci](https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci) (lembrando que em Python os índices começam em 0):

pass

1.15. Escreva uma função que calcule o raio de um círculo, dado um valor de raio. Peça um valor de raio ao usuário e calcule o valor da função.

pass

1.16. Escreva uma função que recebe uma lista e um valor e retorna uma sub-lista apenas com os elementos menores do que o valor fornecido.

pass

1.17. Escreva uma função que calcula a multiplicação de duas matrizes usando laços, mas apenas se as dimensões das matrizes forem compatíveis.

pass

1.18. Escreva uma função que recebe um número e valores de média e de variância e calcula a fdp das distribuições normais correspondentes às médias e às variâncias fornecidas.

pass

1.19. Escreva uma função que verifica se um número é primo.

pass

1.20. Faça uma função que retorna todos os divisores de um número.

pass

1.21. Faça uma função que calcula o fatorial de um número.

pass

1.22. Faça uma função que calcula $P(X = x)$, tal que $X \sim Binomial(n, p)$. Escreva uma função auxiliar que calcula ${n}\choose{x}$ para chamar na função principal.

pass

1.23. Escreva uma função que calcula $P(X = x)$ ou $P(X <= x)$ (o usuário escolhe), tal que $X \sim Binomial(n, p)$.

pass

1.24. Escreva uma função que recebe uma lista, um valor e uma função de comparação e retorna uma sub-lista apenas com os elementos para os quais a função fornecida retorna **True**.

pass

1.25. (Desafio: Recursão). Recursão é uma abordagem para solucionar problemas que envolve dividir a tarefa em partes menores do mesmo tipo, i.e. é uma abordagem do tipo dividir-para-conquistar. Do ponto de vista computacional, um problema resolvido usando recursão envolve uma função que chama a si mesma até que o problema seja resolvido. Uma parte importante desse tipo de solução é a definição do ponto de parada da recursão, quando a função para de chamar a si mesma e começar a retornar os valores para as chamadas mais "acima". Vejamos um exemplo de recursão para o cálculo do fatorial de um número *n*:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(0), factorial(1), factorial(5)

Agora implemente uma função recursiva que recebe um número e retorna o número correspondente na sequência de Fibonacci.

pass

1.26. (Algoritmo de ordenação: Bubble sort). Bubble sort é um algoritmo muito simples. Ele começa no início da lista e compara os dois primeiros elementos. Se o primeiro for maior do que o segundo, eles são trocados. Esse processo se repete para cada par subsequente, até o final da lista. Depois o algoritmo volta ao início da lista e recomeça o processo, repetindo-o até não haver mais trocas. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo bubble sort.

pass

1.27. (Algoritmo de ordenação: Insertion sort). Algoritmo relativamente eficiente para listas pequenas e comumente usado como parte de algoritmos mais sofisticados. Ele funciona da seguinte maneira: a cada iteração, o algoritmo remove um elemento da lista, encontra seu lugar na lista ordenada e insere o elemento. Assim, a parte ordenada da lista cresce a cada iteração. A ordenação é feita na própria lista. A cada posição da lista, o algoritmo compara seu valor com o maior valor da parte ordenada. Se for maior, o elemento é mntido e o algoritmo passa para a próxima posição. Se for menor, ele acha a posição correta do elemento na parte ordenada e move todos os valores maiores para abrir espaço e inserir o elemento. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo insertion sort.

pass       

1.28. (Algoritmo de ordenação: Selection sort). O selection sort divide o array de entrada em duas partes: a parte ordenada, que ocupa a extremidade esquerda do array, e a parte não-ordenada, que ocupa a parte direita do array. O algoritmo busca o menor elemento da parte não-ordenada e o troca com o elemento mais à esquerda da parte não-ordenada, movendo a fronteira entre as duas partes do array uma posição para a direita. O selection sort é quadrático em todos os casos. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo selection sort.

pass             

1.29. (Algoritmo de ordenação: Merge sort). Usa a abordagem dividir para conquistar, aproveitando-se da facilidade de unir duas listas ordenadas em uma nova lista. O algoritmo divide a lista em n listas, cada uma com um elemeno. Uma lista com 1 elemento é considerada ordenada. Depois, o algoritmo repetidamente une arrays adjacentes, produzindo novos arrays ordenados, até que o único array restante contenha todos os elementos ordenados. Para unir dois arrays ordenados, o algoritmo seleciona o menor elemento de cada array e os compara, colocando o menor na primeira posição livre do novo array, e comparando o elemento que sobrou com o novo menor elemento do outro array e assim sucessivamente. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo merge sort.         

pass

1.30. (Algoritmo de ordenação: Quicksort). Assim como o merge sort, o quicksort é um algoritmo que usa a abordagem dividir para conquistar, mais especificamente, uma abordagem de partição. O algoritmo seleciona um elemento, chamado de pivô, e coloca todos os elementos menores do que o pivô antes dele e todos os maiores depois dele. Os dois sub-arrays são então recursivamente ordenados, seguindo o mesmo processo. Implementações eficientes do quicksort estão entre os algoritmos de ordenação mais rápidos na prática. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo quicksort. 

pass

