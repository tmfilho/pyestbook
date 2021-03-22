# Operadores


## Operadores lógicos

Python oferece três operadores lógicos (*booleanos*): **or** (ou), **and** (e) e **not** (não). Os primeiros dois operadores (**or** e **and**) recebem dois operandos e retornam um valor lógico **True** (Verdadeiro) ou **False** (Falso). O terceiro operador (**not**) recebe apenas um operando e retorna o valor lógico oposto. A tabela verdade abaixo apresenta os valores retornados pelos operadores para diferentes valores dos operandos.

| x         | y         | **not** x | x **or** y| x **and** y |
| --------- |:---------:| ---------:| ---------:| -----------:|
| **True**  | **True**  | **False** | **True**  | **True**    |
| **True**  | **False** | **False** | **True**  | **False**   |
| **False** | **True**  | **True**  | **True**  | **False**   |
| **False** | **False** | **True**  | **False** | **False**   |

O operador **or** só retorna **False** se os dois operandos forem falsos, portanto por uma questão de eficiência, Python apenas avalia o segundo operando, se o primeiro for **False**. Por outro lado, o operador **and** só retorna **True** se os dois operandos forem verdadeiros, então Python só avalia o segundo operando se o primeiro for **True**. Por isso, esses operadores são chamados de operadores de curto-circuito e essa característica pode ser usada para otimizar código, colocando operandos menos custosos no lado esquerdo desses operadores.


## Operadores relacionais

O(a) usuário(a) de Python tem oito operadores de comparação (operadores relacionais) a sua disposição, descritos na Tabela abaixo. Os dois últimos operadores são casos especiais de igualdade e diferença para objetos que investigaremos mais à frente no livro. Também veremos mais à frente que objetos de diferentes tipos (exceto números) nunca serão iguais

| Operador         | Significado         |
| --------- |---------|
| <, >  | menor/maior que |
| <=, >=  | menor/maior ou igual a |
| ==, != | igual/diferente  |
| **is**, **is** **not** | igualdade/diferença de objetos |

Comparações podem ser encadeadas livremente, o que permite verificar, por exemplo, se o valor de uma variável *y* cai dentro do intervalo *(0, 3]* da seguinte maneira:

y = 2

0 < y <= 3

O código acima é equivalente ao código abaixo, que corresponde a uma forma mais comum em outras linguagens de programação. No entanto, no formato encadeado acima, a variável *y* é avaliada apenas uma vez, o que produz um código mais eficiente. Além disso, como essas comparações incluem um **and**, a segunda parte (*y <= 3*) só será avaliada se a primeira (*0 < y*) for **True**.

0 < y and y <= 3

## Operadores aritméticos

Python suporta diferentes tipos de números, mas os principais são os inteiros (**int**) e pontos flutuantes (**float**). Além disso, valores lógicos (**bool**) são um subtipo dos inteiros, com **True** equivalendo a *1* e **False** a *0*. Tipos númericos diferentes podem ser usados em uma mesma operação aritmética, com a resposta pertencendo ao tipo mais geral. Os operadores aritméticos incluem:

| Operador  |   Exemplo  | Resultado |
|-----------|------------|-----------|
|   x + y   |    1 + 2   |     3     |
|   x + y   |  True + 2  |     3     |
|   x - y   |   2 - 1.2  |    0.8    |
|   x * y   |   2 * 1e-1 |    0.2    |
|   x / y   |    1 / 2   |    0.5    |
|  x // y   |  10 // 6   |     1     |
|  x // y   |   7 // 2   |     3     |
|   x % y   |    7 % 2   |     1     |
|   x % y   |    6 % 2   |     0     |
| x \*\* y  |  6 \*\*2   |    36     |
|     -x    |     -6     |     -6    |

## Prioridade de operadores

Assim como na matemática, operadores seguem uma ordem de precedência. Naturalmente, é possível realizar operações na ordem desejada com o uso de parênteses. A tabela abaixo apresenta os operadores em ordem crescente de precedência, com operadores na mesma linha recebendo a mesma prioridade. Alguns desses operadores ainda serão vistos neste material.

| Operador  |   Descrição  |
|-----------|------------|
|**lambda** |    Expressões lambda   |
| **if - else**|  Expressões condicionais  |
| **or**   |   OU lógico  |
| **and**   |  E lógico|
| **not**   |  NÃO lógico |
|**in**, **not in**, **is**, **is not**, <, <=, >, >=, !=, ==  |  Comparações/pertencimento/identidade |
| +, -  |  Adição/subtração |
| \*, @, /, //, % |  Multiplicações/divisões  |
| -x |  Negativo   |
| \*\*  | Exponenciação  |
|  x\[indice\]  | Indexação de sequências  |
| (expressao) | Expressões entre parênteses  |

