# Conceitos Fundamentais 

1.1. Calcule a área de um círculo de raio 2. Assuma *pi = 3.14*.

radius, pi = 2, 3.14

pi * radius ** 2

1.2. Escreva uma função que verifica se um número é par. Se for, imprima uma mensagem. Se não for, imprima outra mensagem.

def is_even(x):
    if x % 2 == 0:
        print('Number {} is even'.format(x))
    else:
        print('Number {} is odd'.format(x))

is_even(2)
is_even(3)

1.3. No exercício acima, se o número for par, verifique se ele é múltiplo de 4. Se for, exiba uma mensagem diferente.

def is_even(x):
    if x % 2 == 0:
        message = 'Number {} is even'.format(x)
        if x % 4 == 0:
            message = ' '.join([message, 'and is a multiple of 4'])
        print(message)
    else:
        print('Number {} is odd'.format(x))

is_even(2)
is_even(3)
is_even(64)

1.4. Escreva um código que imprima os elementos menores que 5 na seguinte lista:

a = [1, 4, 2, 3, 2, 1, 5, 8, 5, 7, -1, 0, 23]

[x for x in a if x < 5 ]

1.5. Escreva um código que encontra todos os divisores do número 42.

divisors = [i for i in range(1, 43) if 42 % i == 0]

divisors

1.6. Calcule a multiplicação das duas matrizes abaixo sem usar laços:

a = [[2, 3], [4, 2]]
b = [[2, 0], [1, 2]]

print(
    [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1]
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1]
        ]
    ]

)

1.7. Calcule a multiplicação das duas matrizes acima usando laços

mul = [[0 for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        for c in range(2):
            mul[i][c] += a[i][j] * b[j][c]

mul

1.8. Calcule o fatorial de 5 usando algum tipo de laço.

prod = 1

for i in range(1, 6):
    prod *= i

prod

1.9. Dada uma variável $X \sim N(0, 4)$, calcule o valor da fdp para o valor 2.

import math

x, mu, sigma_2 = 2, 0, 4

fdp = (math.e ** (-(x - mu) ** 2 / (2 * sigma_2))) / math.sqrt(2 * math.pi * sigma_2)

fdp

1.10. Calcule a distância Euclidiana dos seguintes vetores:

import math

a, b = [1, 0, 1], [-1, 2, 3]

total = 0

for i in range(len(a)):
    total += (a[i] - b[i]) ** 2
    
print(math.sqrt(total))

1.11. Imprima as potências de 2, começando em $2^0$, enquanto o resultado for menor do que 2000.

v = 1

while v < 2000:
    print(v)
    v *= 2

1.12. Verifique se o número 79 é primo.

number = 2
x = 79

while number < x:
    if x % number == 0:
        print('{} is not prime'.format(x))
        break
    number += 1
else:
    print('{} is prime'.format(x))

1.13. Escreva uma linha de código Python que gere uma lista apenas com os valores divisíveis por 2 e por 5 na lista abaixo:

a = [1, 4, 10, 13, 15, 16, 20, 28, 30]

[x for x in a if x % 2 == 0 and x % 5 == 0]

1.14. Escreva um laço que resulte no elemento de índice 7 da [sequência de Fibonacci](https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci) (lembrando que em Python os índices começam em 0):

first = 0
second = 1

value = 0
for i in range(1, 7):
    value = first + second
    first = second
    second = value

value

1.15. Escreva uma função que calcule o raio de um círculo, dado um valor de raio. Peça um valor de raio ao usuário e calcule o valor da função.

import math

def circle_area(radius):
    return math.pi * radius ** 2

radius = float(input('Type a radius value: '))
circle_area(radius)

1.16. Escreva uma função que recebe uma lista e um valor e retorna uma sub-lista apenas com os elementos menores do que o valor fornecido.

def less_than(l, v):
    return [x for x in l if x < v]

less_than([5, 1, 2, 5, 0, 9, -1, 11, 5, 4], 5)

1.17. Escreva uma função que calcula a multiplicação de duas matrizes usando laços, mas apenas se as dimensões das matrizes forem compatíveis.

def mul(a, b):
    n_cols_a = len(a[0])
    n_rows_b = len(b)
    if n_cols_a == n_rows_b: 
        n_rows_a = len(a) 
        n_cols_b = len(b[0])
        
        mul = [[0 for _ in range(n_cols_b)] for _ in range(n_rows_a)]

        for i in range(n_rows_a):
            for j in range(n_cols_a):
                for c in range(n_cols_b):
                    mul[i][c] += a[i][j] * b[j][c]

        return mul
    else:
        return 'Incompatible dimensions'

a = [[2, 3], [4, 2]]
b = [[2, 0], [1, 2]]
c = [[2, 3], [4, 2], [0, 1]]
d = [[2, 3, 0], [4, 2, 1]]

mul(a, b), mul(c, b), mul(d, a)

1.18. Escreva uma função que recebe um número e valores de média e de variância e calcula a fdp das distribuições normais correspondentes às médias e às variâncias fornecidas.

import math

def normal_fdp(x, mu, sigma_2):
    return (math.e ** (-(x - mu) ** 2 / (2 * sigma_2))) / math.sqrt(2 * math.pi * sigma_2)

def fdp_list(x, means, variances):
    return [normal_fdp(x, mu, sigma_2) for mu, sigma_2 in zip(means, variances)]

fdp_list(2, [0, 2, -1], [1, 0.5, 2])

1.19. Escreva uma função que verifica se um número é primo.

def is_prime(n):
    number = 2
    while number < n:
        if x % number == 0:
            return False
            break
        number += 1
    else:
        return True

is_prime(79), is_prime(100)

1.20. Faça uma função que retorna todos os divisores de um número.

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

divisors(84)

1.21. Faça uma função que calcula o fatorial de um número.

def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

factorial(0), factorial(1), factorial(5)

1.22. Faça uma função que calcula $P(X = x)$, tal que $X \sim Binomial(n, p)$. Escreva uma função auxiliar que calcula ${n}\choose{x}$ para chamar na função principal.

def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))

def binomial(x, n, p):
    return combination(n, x) * p ** x * (1.0 - p) ** (n - x) 

binomial(2, 5, 0.7)

1.23. Escreva uma função que calcula $P(X = x)$ ou $P(X <= x)$ (o usuário escolhe), tal que $X \sim Binomial(n, p)$.

def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))

def binomial(x, n, p, cumulative=False):
    prob = combination(n, x) * p ** x * (1.0 - p) ** (n - x) 
    if cumulative:
        total = 0
        for i in range(x):
            total += combination(n, i) * p ** i * (1.0 - p) ** (n - i)
        prob = total + prob
    return prob

binomial(2, 5, 0.7, cumulative=True)

1.24. Escreva uma função que recebe uma lista, um valor e uma função de comparação e retorna uma sub-lista apenas com os elementos para os quais a função fornecida retorna **True**.

def sub_list(l, target, func):
    return [x for x in l if func(x, target)]

sub_list([5, 1, 2, 5, 0, 9, -1, 11, 5, 4], 5, lambda x,v: x != v)

1.25. (Desafio: Recursão). Recursão é uma abordagem para solucionar problemas que envolve dividir a tarefa em partes menores do mesmo tipo, i.e. é uma abordagem do tipo dividir-para-conquistar. Do ponto de vista computacional, um problema resolvido usando recursão envolve uma função que chama a si mesma até que o problema seja resolvido. Uma parte importante desse tipo de solução é a definição do ponto de parada da recursão, quando a função para de chamar a si mesma e começar a retornar os valores para as chamadas mais "acima". Vejamos um exemplo de recursão para o cálculo do fatorial de um número *n*:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(0), factorial(1), factorial(5)

Agora implemente uma função recursiva que recebe um número e retorna o número correspondente na sequência de Fibonacci.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

fibonacci(0), fibonacci(1), fibonacci(20)

1.26. (Algoritmo de ordenação: Bubble sort). Bubble sort é um algoritmo muito simples. Ele começa no início da lista e compara os dois primeiros elementos. Se o primeiro for maior do que o segundo, eles são trocados. Esse processo se repete para cada par subsequente, até o final da lista. Depois o algoritmo volta ao início da lista e recomeça o processo, repetindo-o até não haver mais trocas. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo bubble sort.

def bubble_sort(l):
    keepSorting = True
    while keepSorting:
        keepSorting = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                temp = l[i + 1]
                l[i + 1] = l[i]
                l[i] = temp
                keepSorting = True
    return l

l = [10, 1, 2, 8, 0, 9, -1, 11, 5, 4]
bubble_sort(l)

1.27. (Algoritmo de ordenação: Insertion sort). Algoritmo relativamente eficiente para listas pequenas e comumente usado como parte de algoritmos mais sofisticados. Ele funciona da seguinte maneira: a cada iteração, o algoritmo remove um elemento da lista, encontra seu lugar na lista ordenada e insere o elemento. Assim, a parte ordenada da lista cresce a cada iteração. A ordenação é feita na própria lista. A cada posição da lista, o algoritmo compara seu valor com o maior valor da parte ordenada. Se for maior, o elemento é mntido e o algoritmo passa para a próxima posição. Se for menor, ele acha a posição correta do elemento na parte ordenada e move todos os valores maiores para abrir espaço e inserir o elemento. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo insertion sort.

def insertion_sort(l):    
    for i in range(1, len(l)):
        key = l[i]
        k =i
        while k > 0 and key < l[k - 1]:
            l[k] = l[k - 1]
            k -= 1
        l[k] = key
    return l

l = [10, 1, 2, 8, 0, 9, -1, 11, 5, 4]
insertion_sort(l) 

1.28. (Algoritmo de ordenação: Selection sort). O selection sort divide o array de entrada em duas partes: a parte ordenada, que ocupa a extremidade esquerda do array, e a parte não-ordenada, que ocupa a parte direita do array. O algoritmo busca o menor elemento da parte não-ordenada e o troca com o elemento mais à esquerda da parte não-ordenada, movendo a fronteira entre as duas partes do array uma posição para a direita. O selection sort é quadrático em todos os casos. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo selection sort.

def selection_sort(l):
    for i in range(len(l) - 1):
        j_minimum = i        
        for j in range(i + 1, len(l)):
            if l[j] < l[j_minimum]:
                j_minimum = j
                
        temp = l[j_minimum]
        l[j_minimum] = l[i]
        l[i] = temp
    return l
            

l = [10, 1, 2, 8, 0, 9, -1, 11, 5, 4]
selection_sort(l)            

1.29. (Algoritmo de ordenação: Merge sort). Usa a abordagem dividir para conquistar, aproveitando-se da facilidade de unir duas listas ordenadas em uma nova lista. O algoritmo divide a lista em n listas, cada uma com um elemeno. Uma lista com 1 elemento é considerada ordenada. Depois, o algoritmo repetidamente une arrays adjacentes, produzindo novos arrays ordenados, até que o único array restante contenha todos os elementos ordenados. Para unir dois arrays ordenados, o algoritmo seleciona o menor elemento de cada array e os compara, colocando o menor na primeira posição livre do novo array, e comparando o elemento que sobrou com o novo menor elemento do outro array e assim sucessivamente. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo merge sort.         

def merge_sort(l):
    if len(l) > 1:
        middle = len(l)//2
        #também é valido: middle = int(len(l)/2)
        left_list = l[:middle]
        right_list = l[middle:]
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                l[k] = left_list[i]
                i += 1
            else:
                l[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):

            l[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            l[k] = right_list[j]
            j += 1
            k += 1
    return l

l = [10, 1, 2, 8, 0, 9, -1, 11, 5, 4]
print(merge_sort(l))

1.30. (Algoritmo de ordenação: Quicksort). Assim como o merge sort, o quicksort é um algoritmo que usa a abordagem dividir para conquistar, mais especificamente, uma abordagem de partição. O algoritmo seleciona um elemento, chamado de pivô, e coloca todos os elementos menores do que o pivô antes dele e todos os maiores depois dele. Os dois sub-arrays são então recursivamente ordenados, seguindo o mesmo processo. Implementações eficientes do quicksort estão entre os algoritmos de ordenação mais rápidos na prática. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo quicksort. 

def quicksort(l, ini, end):
    i = ini
    j = end
    index_pivot = (ini + end) // 2
    pivot = l[index_pivot]
    while i <= j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i <= j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
    if ini < j:
        quicksort(l, ini, j)
    if i < end:
        quicksort(l, i, end)
        
    return l

l = [10, 1, 2, 8, 0, 9, -1, 11, 5, 4]
quicksort(l, 0, len(l) - 1)

