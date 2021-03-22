# Objetos e Classes

A programação orientada a objetos (OOP - do inglês *object oriented programming*) é um paradigma de programação baseado no conceito de objetos, que, na maior parte das linguagens OOP, são manifestações concretas de abstrações, chamadas classes. As classes representam tipos de dados e quais são seus atributos ou propriedades, de forma que cada objeto é uma instância de uma classe e pode ter valores diferentes para seus atributos. Além disso, as classes determinam que ações os seus objetos podem realizar, por meio de funções chamadas de métodos. Os métodos são frequentemente definidos de forma que os dados armazenados nos atributos do objeto associado ou de outro objeto são modificados. Programas OOP são então desenvolvidos por meio da criação e da interação de objetos. Alguns exemplos de classes incluem:

   1. Carro:
      * Atributos:
         1. Marca
         2. Modelo
         3. Ano
         4. Placa
         5. Opcionais (lista)
      * Métodos:
         1. Ligar
         2. Desligar
         3. Acelerar
         4. Frear
         5. Ligar rádio
   2. Distribuição Normal
      * Atributos:
         1. Média
         2. Variância 
      * Métodos
         1. Calcular fdp
         2. Gerar amostra 
         3. Calcular função de distribuição acumulada
   2. Regressão Linear
      * Atributos:
         1. Coeficientes
         2. Intercepto 
      * Métodos
         1. Ajustar a uma amostra
         2. Estimar valores para nova amostra 
         3. Calcular $R^2$
         4. Realizar testes de hipótese

Note que cada classe representa um conceito, sua descrição (atributos) e suas ações associadas (métodos). Assim, um objeto é uma realização concreta de um conceito de classe, i.e. uma instância de classe. Por exemplo: $X \sim N(3, 4)$ é um objeto que é uma instância de distribuição Normal com média *3* e variância *4*. Com esse objeto, podemos calcular o valor da fdp ou da função de distribuição acumulada para um dado valor (ou uma lista de valores) e gerar amostra(s) aleatórias.


## Uma breve discussão sobre escopo

Antes de seguirmos com o estudo de classes e objetos, precisamos discutir o funcionamento de escopos e *namespaces* (espaços de nomes) em Python. Escopo é a região de código em que uma variável ou uma função existe. Cada escopo tem um *namespace* associado, que é o conjunto de nomes de vaiáveis ou funções que pertencem àquele escopo. Os *namespaces* são implementados por meio de dicionários, mas isso não costuma ser perceptível. A qualquer momento durate a execução de um script, existem vários escopos/*namespaces* aninhados e acessíveis:

   * O escopo local
   * O escopo de alguma função que envolva o escopo local
   * O escopo global do script/módulo
   * O escopo mais externo de todos, que contém palavras reservadas e identificadores integrados da linguagem
   
Quando o código tenta acessar um identificador (por exemplo ao chamar uma função), o interpretador de Python busca pelo identificador do *namespace* do escopo mais interno até o mais externo, até encontrá-lo. Veja o seguinte exemplo: 

t = 10

def test():
    t = 5
    print(t)

test()
print(t)

O código acima define uma variável *t* com valor *10* no escopo global e outra variável com o mesmo nome e valor *5* no escopo da função *test*. Ao imprimir o valor de *t* dentro da função, o resultado é *5*. Após a chamada da função, o valor de *t* é impresso novamente, obtendo o valor de *t* no escopo global. Isso acontece porque uma **atribuição** a uma variável em um escopo interno sempre irá criar a variável dentro do *namespace* interno. Note que, se não houver a atribuição *t = 5*, o valor impresso dentro de *test* será o da variável *t* externa.

t = 10

def test():
    print(t)

test()
print(t)

Podemos atribuir um valor à variável *t* do escopo global dentro do escopo da função *test* por meio do operador **global**. Nesse caso, é preciso declarar que a variável é global antes da atribuição. Note a mudança do valor de *t* global após a chamada da função.

t = 10

def test():
    global t
    t = 5
    print(t)

test()
print(t)

Note que o operador **global** faz com que a variável *t* "viva" no escopo global, o que permite que ela seja criada dentro da função e passe a existir no escopo global após a sua chamada.

def test():
    global x
    x = 5
    print(x)

test()
print(x)

Agora observe o seguinte exemplo:

t = 10

def test():
    global t
    t = 5
    def test_nested():
        t = 3
        print(t)
    test_nested()
    print(t)

test()
print(t)

Há 3 atribuições à variável *t* no código acima. Na função *test*, o operador **global** faz com que a atribuição *t = 5* seja aplicada à variável *t* global. Mas isso não afeta a atribuição *t = 3* da função aninhada *test_nested*. Para que a terceira atribuiçãose aplique à mesma variável, é necessário usar **global** novamente. 

t = 10

def test():
    global t
    t = 5
    def test_nested():
        global t
        t = 3
        print(t)
    test_nested()
    print(t)

test()
print(t)

O operador **global**, como seu nome indica, só se aplica a variáveis do escopo global. Se a variável *t* tivesse sido definida na função *test*, a função *test_nested* não poderia atribuir um valor a ela por meio do uso de **global**. Exemplo:

def test():
    t = 5
    def test_nested():
        global t
        t = 3
        print(t)
    test_nested()
    print(t)

test()
print(t)

Note que no código acima, a linha **global** *t* dentro de *test_nested* cria uma nova variável global e não modifica a variável *t* criada por *test*. Caso deseje-se modificar o valor da variável *t* definida no escopo acima, usa-se o operador **nonlocal**:

def test():
    t = 5
    def test_nested():
        nonlocal t
        t = 3
        print(t)
    test_nested()
    print(t)

test()

Outro exemplo, retirado da [documentação de Python](https://docs.python.org/3/tutorial/classes.html).

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)




```{toctree}
:hidden:
:titlesonly:


02_cpyt
03_inhe
04_erro
05_exer
```
